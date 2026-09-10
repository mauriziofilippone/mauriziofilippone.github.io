---
permalink: /
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
.highlight-card {
  display: flex;
  gap: 1.4rem;
  align-items: flex-start;
  background: var(--background-color, #fff);
  border: 1px solid var(--border-color, #ddd);
  border-radius: 8px;
  padding: 1.2rem 1.4rem;
  margin: 1.2rem 0 2rem 0;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
.highlight-thumb {
  flex: 0 0 140px;
  width: 140px;
}
.highlight-thumb img {
  width: 100%;
  border-radius: 4px;
  display: block;
  border: 1px solid var(--border-color, #e0e0e0);
}
.highlight-body {
  flex: 1;
  min-width: 0;
}
.highlight-badge {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  padding: 0.15rem 0.6rem;
  border-radius: 2rem;
  border: 1px solid var(--border-color, #ccc);
  color: inherit;
  text-decoration: none;
  margin-bottom: 0.55rem;
  opacity: 0.75;
}
.highlight-title {
  font-size: 1rem;
  font-weight: 600;
  margin: 0 0 0.3rem 0;
  line-height: 1.35;
}
.highlight-citation {
  font-size: 0.82rem;
  opacity: 0.7;
  margin: 0 0 0.5rem 0;
}
.highlight-desc {
  font-size: 0.88rem;
  line-height: 1.55;
  margin: 0 0 0.75rem 0;
}
.highlight-links {
  font-size: 0.85rem;
}
.highlight-links a {
  margin-right: 1rem;
  text-decoration: none;
}
.highlight-links a:hover { text-decoration: underline; }
.highlight-day-label {
  font-size: 0.78rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  opacity: 0.5;
  margin-bottom: 0.4rem;
}
@media (max-width: 540px) {
  .highlight-card { flex-direction: column; }
  .highlight-thumb { width: 100%; flex: none; }
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) .highlight-card {
    background: #1e1e1e;
    border-color: #3a3a3a;
    box-shadow: 0 1px 4px rgba(0,0,0,0.4);
    color: #e0e0e0;
  }
  :root:not([data-theme="light"]) .highlight-thumb img {
    border-color: #3a3a3a;
  }
}
:root[data-theme="dark"] .highlight-card {
  background: #1e1e1e;
  border-color: #3a3a3a;
  box-shadow: 0 1px 4px rgba(0,0,0,0.4);
  color: #e0e0e0;
}
:root[data-theme="dark"] .highlight-thumb img {
  border-color: #3a3a3a;
}
</style>

I am an Associate Professor of Statistics at [KAUST](https://www.kaust.edu.sa/), Saudi Arabia. Before joining KAUST, I held faculty positions at EURECOM (France) and at the University of Glasgow (UK). My research is at the intersection between Statistics and Machine Learning and it focuses on the mathematical and computational aspects of Bayesian statistics applied to Deep Learning and Gaussian process-based models. The motivation is that uncertainty quantification is of fundamental importance to enable sound decision making. Check out the [research section](./research/) for more details. 

## Research Highlight

<div class="highlight-day-label" id="highlight-label"></div>
<div class="highlight-card" id="highlight-card">
  <div class="highlight-thumb"><div style="width:140px;height:105px;background:#f0f0f0;border-radius:4px;"></div></div>
  <div class="highlight-body"><p style="opacity:0.4;font-size:0.9rem;margin:0">Loading…</p></div>
</div>

<script src="/assets/js/research-highlight.js"></script>

## News

{% for post in site.posts limit:15 %}<p><strong>{{ post.date | date: "%d-%m-%y" }}</strong> &mdash; {{ post.content | remove: '<p>' | remove: '</p>' | strip_newlines }}</p>
{% endfor %}

[... older news](/news/)
