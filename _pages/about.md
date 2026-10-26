---
layout: about
title: about
nav_title: "<span class='lang-en'>about</span><span class='lang-zh'>关于</span>"
permalink: /
title_zh: 北航集成功率电子与系统实验室
title_en_full: Beihang Integrated Power Electronics and Systems (BiPES) Lab

# No page.profile card here — the PI photo/contact info lives in the
# #members section below (_data/members.yml + _includes/members/member_tong.md)
# instead of being duplicated at the top of the page.

# selected_papers / announcements are placed by hand in the #publications and
# #news sections below instead of letting the `about` layout auto-append them
# after {{ content }}, so they land in nav order on this single-scroll page.
selected_papers: false
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false
  scrollable: false
  limit: 3

latest_posts:
  enabled: false
  scrollable: true
  limit: 3
---

{% include hero-carousel.liquid %}

<div class="lang-en" markdown="1">
The **BiPES Lab** (Beihang Integrated Power Electronics and Systems Lab) is based at the School of Integrated Circuit Science and Engineering, Beihang University. We focus on **power management integrated circuits and systems**, developing high-performance power IC solutions for data centers and other emerging applications. We also explore AI-assisted power chip design (**AI for Power**), advancing the integration of power chips and AI methods.

</div>

<div class="lang-zh" markdown="1">
**北航集成功率电子与系统实验室（BiPES Lab）** 依托北京航空航天大学集成电路科学与工程学院组建。实验室专注于 **电源管理集成电路与系统** 研究，致力于为数据中心等前沿应用提供高性能电源芯片解决方案；同时探索以人工智能方法赋能电源芯片设计（**AI for Power**），推动电源芯片与 AI 方法的深度融合。

</div>

<section id="news">
  <div class="news-section-heading">
    <h2><span class="lang-en">News</span><span class="lang-zh">新闻动态</span></h2>
    <a href="{{ '/news/' | relative_url }}"><span class="lang-en">View all &rarr;</span><span class="lang-zh">查看更多 &rarr;</span></a>
  </div>
  {% include news.liquid limit=true %}
</section>

<section id="members">
  <h2><span class="lang-en">Members</span><span class="lang-zh">成员</span></h2>
  {% include members-section.liquid %}
</section>

<section id="projects">
  <div class="news-section-heading">
    <h2><span class="lang-en">Selected Projects</span><span class="lang-zh">精选项目</span></h2>
    <a href="{{ '/project-showcase/' | relative_url }}">
      <span class="lang-en">See all projects &rarr;</span>
      <span class="lang-zh">查看全部项目 &rarr;</span>
    </a>
  </div>
  {% include project-showcase.liquid %}
</section>

<section id="publications">
  <div class="news-section-heading">
    <h2><span class="lang-en">Selected Publications</span><span class="lang-zh">精选论文</span></h2>
    <a href="{{ '/publications/' | relative_url }}">
      <span class="lang-en">See all publications &rarr;</span>
      <span class="lang-zh">查看全部论文 &rarr;</span>
    </a>
  </div>
  {% include selected_papers.liquid %}
</section>

<section id="join-us">
  <h2><span class="lang-en">Join Us</span><span class="lang-zh">加入我们</span></h2>
  {% include join-us-content.liquid %}
</section>
