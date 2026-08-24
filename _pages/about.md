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
  scrollable: true
  limit: 5

latest_posts:
  enabled: false
  scrollable: true
  limit: 3
---

<div class="lang-en" markdown="1">
The **BiPES Lab** (Beihang Integrated Power Electronics and Systems Lab) is established at the School of Integrated Circuit Science and Engineering, Beihang University (BUAA), led by Prof. Zhiguo Tong. We work on **power management integrated circuits and systems**, delivering high-performance power IC solutions for applications — data center computing, robotic electromechanical systems, and space/extreme-radiation environments — that demand the utmost in power conversion efficiency, power density, and reliability. We also explore AI-assisted power chip design (**AI for Power**), advancing the convergence of power electronics with intelligent design methods.

- **Data Center Power Delivery** — high-efficiency, high-density hybrid DC-DC converters for rack-to-chip and on-package power delivery.
- **Robot Joint Motor Drive Circuits** — high-voltage power transmission cables and motor-drive power stages for humanoid/legged robots.
- **Radiation-Hardened Power Circuits** — radiation-tolerant converter topologies for satellite and aerospace platforms.
- **AI-Assisted Power Chip Design** — machine-learning-assisted design-space exploration for power ICs.

</div>

<div class="lang-zh" markdown="1">
**北航集成功率电子与系统实验室（BiPES Lab）** 依托北京航空航天大学集成电路科学与工程学院组建。实验室专注于 **电源管理集成电路与系统** 研究，致力于为数据中心算力、机器人机电系统、空间及极端辐照环境等对电能变换效率、功率密度与可靠性有极致要求的场景，提供高性能电源芯片解决方案；同时探索以人工智能方法赋能电源芯片设计（**AI for Power**），推动电源电子技术与智能化设计方法的深度融合。

- **数据中心供电技术** —— 面向机架到芯片及封装内供电的高效率、高密度混合型 DC-DC 变换器。
- **机器人关节电机驱动电路** —— 面向人形/腿式机器人的高压电源传输线缆与关节电机驱动电源级。
- **抗辐照电源电路** —— 面向卫星及航空航天平台的抗辐照变换器拓扑。
- **AI 辅助电源芯片设计** —— 基于机器学习辅助的电源芯片设计空间搜索与优化。

</div>

<section id="research">
  <h2><span class="lang-en">Research</span><span class="lang-zh">研究方向</span></h2>
  {% include research-cards.liquid %}
</section>

<section id="news">
  <h2><span class="lang-en">News</span><span class="lang-zh">新闻动态</span></h2>
  {% include news.liquid %}
</section>

<section id="members">
  <h2><span class="lang-en">Members</span><span class="lang-zh">成员</span></h2>
  {% include members-section.liquid %}
</section>

<section id="projects">
  <h2><span class="lang-en">Projects</span><span class="lang-zh">项目展示</span></h2>
  {% include project-showcase.liquid %}
</section>

<section id="publications">
  <h2><span class="lang-en">Selected Publications</span><span class="lang-zh">精选论文</span></h2>
  {% include selected_papers.liquid %}
  <p>
    <a href="{{ '/publications/' | relative_url }}">
      <span class="lang-en">See all publications &rarr;</span>
      <span class="lang-zh">查看全部论文 &rarr;</span>
    </a>
  </p>
</section>

<section id="join-us">
  <h2><span class="lang-en">Join Us</span><span class="lang-zh">加入我们</span></h2>
  {% include join-us-content.liquid %}
</section>
