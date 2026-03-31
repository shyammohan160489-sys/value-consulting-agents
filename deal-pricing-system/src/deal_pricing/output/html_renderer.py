"""HTML output renderer using Jinja2 templates."""

from __future__ import annotations

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from ..engine.comparator import format_currency, format_pct
from ..models.output import DealPackage


# Inline template — avoids dependency on external template files
DEAL_MEMO_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ title }}</title>
<style>
  :root {
    --bb-primary: #1A1F71;
    --bb-accent: #00B4D8;
    --bb-dark: #0D1117;
    --bb-gray: #6B7280;
    --bb-light: #F3F4F6;
    --bb-green: #10B981;
    --bb-red: #EF4444;
    --bb-yellow: #F59E0B;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    color: var(--bb-dark);
    line-height: 1.6;
    background: #fff;
  }
  .page { max-width: 900px; margin: 0 auto; padding: 40px; }

  /* Header */
  .header {
    background: var(--bb-primary);
    color: white;
    padding: 40px;
    border-radius: 8px;
    margin-bottom: 32px;
  }
  .header h1 { font-size: 28px; font-weight: 700; margin-bottom: 8px; }
  .header .subtitle { font-size: 16px; opacity: 0.85; }
  .header .meta { margin-top: 16px; font-size: 13px; opacity: 0.7; }

  /* Sections */
  .section { margin-bottom: 32px; }
  .section-title {
    font-size: 18px;
    font-weight: 700;
    color: var(--bb-primary);
    border-bottom: 2px solid var(--bb-accent);
    padding-bottom: 8px;
    margin-bottom: 16px;
  }
  .section p { margin-bottom: 12px; color: #374151; }

  /* KPI Cards */
  .kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 32px;
  }
  .kpi-card {
    background: var(--bb-light);
    border-radius: 8px;
    padding: 20px;
    text-align: center;
  }
  .kpi-card .label { font-size: 12px; color: var(--bb-gray); text-transform: uppercase; letter-spacing: 0.5px; }
  .kpi-card .value { font-size: 24px; font-weight: 700; color: var(--bb-primary); margin-top: 4px; }
  .kpi-card .delta { font-size: 13px; margin-top: 4px; }
  .kpi-card .delta.positive { color: var(--bb-green); }
  .kpi-card .delta.negative { color: var(--bb-red); }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 16px;
    font-size: 14px;
  }
  th {
    background: var(--bb-primary);
    color: white;
    padding: 10px 14px;
    text-align: left;
    font-weight: 600;
  }
  th.right, td.right { text-align: right; }
  td { padding: 10px 14px; border-bottom: 1px solid #E5E7EB; }
  tr:last-child td { border-bottom: none; }
  tr.total td { font-weight: 700; background: var(--bb-light); }

  /* Construct box */
  .construct-box {
    background: var(--bb-light);
    border-left: 4px solid var(--bb-accent);
    padding: 20px;
    border-radius: 0 8px 8px 0;
    margin-bottom: 16px;
  }
  .construct-box h3 { color: var(--bb-primary); margin-bottom: 8px; }
  .construct-box .badge {
    display: inline-block;
    background: var(--bb-accent);
    color: white;
    padding: 2px 10px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 8px;
  }

  /* Pros/Cons */
  .proscons { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 12px; }
  .proscons ul { list-style: none; padding: 0; }
  .proscons li { padding: 4px 0; font-size: 14px; }
  .proscons .pro li::before { content: "✓ "; color: var(--bb-green); font-weight: 700; }
  .proscons .con li::before { content: "✗ "; color: var(--bb-red); font-weight: 700; }

  /* Objections */
  .objection { margin-bottom: 16px; }
  .objection .q { font-weight: 600; color: var(--bb-primary); margin-bottom: 4px; }
  .objection .a { color: #374151; }
  .objection .data { font-size: 13px; color: var(--bb-gray); font-style: italic; margin-top: 4px; }

  /* Next Steps */
  .step-row { display: flex; gap: 16px; padding: 12px 0; border-bottom: 1px solid #E5E7EB; align-items: flex-start; }
  .step-num {
    background: var(--bb-primary);
    color: white;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    font-weight: 700;
    flex-shrink: 0;
  }
  .step-content { flex: 1; }
  .step-content .title { font-weight: 600; }
  .step-content .meta { font-size: 13px; color: var(--bb-gray); }

  /* Footer */
  .footer {
    margin-top: 48px;
    padding-top: 24px;
    border-top: 1px solid #E5E7EB;
    font-size: 12px;
    color: var(--bb-gray);
    text-align: center;
  }

  @media print {
    .page { padding: 20px; }
    .kpi-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>
</head>
<body>
<div class="page">

  <!-- Header -->
  <div class="header">
    <h1>{{ pkg.deal_brief.client.name }}</h1>
    <div class="subtitle">{{ pkg.deal_context.deal_classification }}</div>
    <div class="meta">
      Deal {{ pkg.deal_brief.deal_id }} &middot;
      {{ pkg.deal_brief.deal_type.value | replace('_', ' ') | title }} &middot;
      {{ ', '.join(segments) }} &middot;
      Generated {{ pkg.generated_at[:10] }}
    </div>
  </div>

  <!-- Executive Summary -->
  <div class="section">
    <div class="section-title">Executive Summary</div>
    <p>{{ pkg.narrative.executive_summary }}</p>
  </div>

  <!-- KPI Cards -->
  <div class="kpi-grid">
    <div class="kpi-card">
      <div class="label">Recommended ARR (Y1)</div>
      <div class="value">{{ kpi.rec_arr_y1 }}</div>
      <div class="delta positive">{{ kpi.arr_uplift }}</div>
    </div>
    <div class="kpi-card">
      <div class="label">5-Year Deal Value</div>
      <div class="value">{{ kpi.deal_value_5yr }}</div>
      <div class="delta positive">{{ kpi.total_uplift }}</div>
    </div>
    <div class="kpi-card">
      <div class="label">Avg $/User</div>
      <div class="value">{{ kpi.avg_per_user }}</div>
    </div>
    <div class="kpi-card">
      <div class="label">ARR CAGR</div>
      <div class="value">{{ kpi.arr_cagr }}</div>
    </div>
  </div>

  <!-- Deal Context -->
  <div class="section">
    <div class="section-title">Deal Context</div>
    <p>{{ pkg.narrative.deal_context_recap }}</p>
    <p><strong>Client pressure points:</strong> {{ '; '.join(pkg.deal_context.client_pressure_points) }}</p>
    <p><strong>Backbase objectives:</strong> {{ '; '.join(pkg.deal_context.backbase_pressure_points) }}</p>
  </div>

  <!-- Pricing Construct -->
  <div class="section">
    <div class="section-title">Recommended Pricing Construct</div>
    <div class="construct-box">
      <span class="badge">{{ pkg.pricing_strategy.recommended.construct_type.value | replace('_', ' ') | upper }}</span>
      <h3>{{ pkg.pricing_strategy.recommended.label }}</h3>
      <p>{{ pkg.narrative.construct_explanation }}</p>
      <div class="proscons">
        <div class="pro">
          <strong>Client Benefits</strong>
          <ul>{% for p in pkg.pricing_strategy.recommended.pros_client %}<li>{{ p }}</li>{% endfor %}</ul>
        </div>
        <div class="con">
          <strong>Client Considerations</strong>
          <ul>{% for c in pkg.pricing_strategy.recommended.cons_client %}<li>{{ c }}</li>{% endfor %}</ul>
        </div>
      </div>
    </div>
    {% if pkg.pricing_strategy.alternative %}
    <div class="construct-box" style="border-left-color: var(--bb-gray);">
      <span class="badge" style="background: var(--bb-gray);">ALTERNATIVE</span>
      <h3>{{ pkg.pricing_strategy.alternative.label }}</h3>
      <p>{{ pkg.pricing_strategy.alternative.description }}</p>
    </div>
    {% endif %}
    <p><strong>Rationale:</strong> {{ pkg.pricing_strategy.rationale }}</p>
  </div>

  <!-- Financial Projections — Recommended -->
  <div class="section">
    <div class="section-title">Financial Projections — Recommended</div>
    <table>
      <thead>
        <tr>
          <th>Year</th>
          <th class="right">Users</th>
          <th class="right">License</th>
          <th class="right">Services</th>
          <th class="right">Total</th>
          <th class="right">$/User</th>
          <th class="right">ARR</th>
        </tr>
      </thead>
      <tbody>
        {% for y in pkg.financials.recommended.yearly %}
        <tr>
          <td>Y{{ y.year }}</td>
          <td class="right">{{ "{:,}".format(y.users) }}</td>
          <td class="right">{{ fc(y.license_revenue) }}</td>
          <td class="right">{{ fc(y.services_revenue) }}</td>
          <td class="right">{{ fc(y.total_revenue) }}</td>
          <td class="right">{{ fc(y.per_user_cost, 2) }}</td>
          <td class="right">{{ fc(y.arr) }}</td>
        </tr>
        {% endfor %}
        <tr class="total">
          <td>Total</td>
          <td class="right"></td>
          <td class="right">{{ fc(pkg.financials.recommended.total_license_5yr) }}</td>
          <td class="right">{{ fc(pkg.financials.recommended.total_services_5yr) }}</td>
          <td class="right">{{ fc(pkg.financials.recommended.total_deal_value_5yr) }}</td>
          <td class="right">{{ fc(pkg.financials.recommended.avg_per_user_5yr, 2) }}</td>
          <td class="right"></td>
        </tr>
      </tbody>
    </table>
  </div>

  {% if pkg.financials.alternative %}
  <!-- Financial Projections — Alternative -->
  <div class="section">
    <div class="section-title">Financial Projections — Alternative</div>
    <table>
      <thead>
        <tr>
          <th>Year</th>
          <th class="right">Users</th>
          <th class="right">License</th>
          <th class="right">Services</th>
          <th class="right">Total</th>
          <th class="right">$/User</th>
          <th class="right">ARR</th>
        </tr>
      </thead>
      <tbody>
        {% for y in pkg.financials.alternative.yearly %}
        <tr>
          <td>Y{{ y.year }}</td>
          <td class="right">{{ "{:,}".format(y.users) }}</td>
          <td class="right">{{ fc(y.license_revenue) }}</td>
          <td class="right">{{ fc(y.services_revenue) }}</td>
          <td class="right">{{ fc(y.total_revenue) }}</td>
          <td class="right">{{ fc(y.per_user_cost, 2) }}</td>
          <td class="right">{{ fc(y.arr) }}</td>
        </tr>
        {% endfor %}
        <tr class="total">
          <td>Total</td>
          <td class="right"></td>
          <td class="right">{{ fc(pkg.financials.alternative.total_license_5yr) }}</td>
          <td class="right">{{ fc(pkg.financials.alternative.total_services_5yr) }}</td>
          <td class="right">{{ fc(pkg.financials.alternative.total_deal_value_5yr) }}</td>
          <td class="right">{{ fc(pkg.financials.alternative.avg_per_user_5yr, 2) }}</td>
          <td class="right"></td>
        </tr>
      </tbody>
    </table>
  </div>
  {% endif %}

  <!-- Objection Handling -->
  {% if pkg.narrative.objections %}
  <div class="section">
    <div class="section-title">Objection Handling</div>
    {% for obj in pkg.narrative.objections %}
    <div class="objection">
      <div class="q">Q: {{ obj.objection }}</div>
      <div class="a">{{ obj.response }}</div>
      {% if obj.supporting_data %}<div class="data">{{ obj.supporting_data }}</div>{% endif %}
    </div>
    {% endfor %}
  </div>
  {% endif %}

  <!-- Next Steps -->
  {% if pkg.narrative.next_steps %}
  <div class="section">
    <div class="section-title">Next Steps</div>
    {% for step in pkg.narrative.next_steps %}
    <div class="step-row">
      <div class="step-num">{{ loop.index }}</div>
      <div class="step-content">
        <div class="title">{{ step.step }}</div>
        <div class="meta">{{ step.owner }} &middot; {{ step.timeline }}</div>
      </div>
    </div>
    {% endfor %}
  </div>
  {% endif %}

  <!-- Footer -->
  <div class="footer">
    Backbase Deal Pricing System &middot; Confidential &middot; Generated {{ pkg.generated_at[:10] }}
  </div>

</div>
</body>
</html>
"""


def render_html(package: DealPackage, output_path: Path) -> Path:
    """Render a deal package to HTML."""
    env = Environment(autoescape=select_autoescape(["html"]))
    template = env.from_string(DEAL_MEMO_TEMPLATE)

    rec = package.financials.recommended
    base = package.financials.baseline

    kpi = {
        "rec_arr_y1": format_currency(rec.arr_year_1),
        "deal_value_5yr": format_currency(rec.total_deal_value_5yr),
        "avg_per_user": format_currency(rec.avg_per_user_5yr, decimals=2),
        "arr_cagr": format_pct(rec.arr_cagr * 100),
        "arr_uplift": f"{format_pct(package.financials.arr_uplift_pct)} vs baseline",
        "total_uplift": f"{format_currency(package.financials.total_uplift_abs)} vs baseline",
    }

    segments = [s.value.title() for s in package.deal_brief.client.segments]

    html = template.render(
        pkg=package,
        kpi=kpi,
        segments=segments,
        title=f"Deal Memo — {package.deal_brief.client.name}",
        fc=format_currency,
        fp=format_pct,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    return output_path
