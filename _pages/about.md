---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
My research focuses on mining softare repositories (e.g., bug reports, GitHub data) to uncover interesting and actionable information to help improve software quality and developer productivity. I have employed and developed techniques including natural language processing, machine learning, and program analysis to transform passive software engineering data into new insights and automated tools like bug triaging and bug localization tools.

I am actively recruiting graduate students, typically enrolling 2-3 each year. Please contact me if you are interested in mining software repositories, empirical software engineering, and artificial intelligence for software engineering.



<span class='anchor' id='education-and-employment'></span>
# 🎓 Education & Employment

- *03/2020 - Now*, <a href="http://nuaa.edu.cn/"><img class="svg" src="/images/logos/NUAA_logo.svg" width="20pt"></a> Nanjing University of Aeronautics and Astronautics, Associate Professor
- *09/2017 - 09/2018*, <a href="https://www.smu.edu.sg/"><img class="svg" src="/images/logos/SMU_logo.svg" width="60pt"></a> Singapore Management University, Visting Student Supported by CSC, Advisor: [David Lo](http://www.mysmu.edu/faculty/davidlo/)
- *09/2015 - 12/2019*, <a href="https://www.nju.edu.cn/en/"><img class="svg" src="/images/logos/NJU_logo.svg" width="20pt"></a> Nanjing University, Ph.D, Software Engineering, Advisors: [Baowen Xu](https://cs.nju.edu.cn/xubaowen/), [Zhenyu Chen](https://software.nju.edu.cn/zychen/)
- *07/2013 - 07/2015*, <a href="https://e.jxust.edu.cn/"><img class="svg" src="/images/logos/JXUST_logo.svg" width="20pt"></a> JiangXi University of Science and Technology, Assistant Professor
- *09/2010 - 06/2013*, <a href="https://en.dlut.edu.cn/"><img class="svg" src="/images/logos/DLUT_logo.svg" width="20pt"></a> Dalian University of Technology, Master, Computer Science and Technology, Advisors: [Yan Hu](http://oscar-lab.org/people/~yhu/), [He Jiang](https://faculty.dlut.edu.cn/jianghe/zh_CN/index.htm)
- *09/2006 - 06/2010*, <a href="https://en.dlut.edu.cn/"><img class="svg" src="/images/logos/DLUT_logo.svg" width="20pt"></a> Dalian University of Technology, Bachelor, Software Engineering (Intensive Japanese)



<span class='anchor' id='publications'></span>
# 📝 Publications
<table border="0">
  <tr><span>
    <td valign="top" width="110" id="IST25">[IST25]</td>
    <td valign="top">Hui Xu<sup>1</sup>, Zhaodan Wang<sup>1</sup>, <b>Weiqin Zou*</b>. "A More Accurate Bug Localization Technique for Bugs with Multiple Buggy Code Files". Information and Software Technology (2025).
    <span>[<a href="papers/IST2025.pdf">Paper</a>]</span></td>
  </span></tr>
  
  <tr><span>
    <td valign="top" width="110" id="SQJ24">[SQJ24]</td>
    <td valign="top">Qianshaung Meng, <b>Weiqin Zou*</b>, Biyu Cai, Jingxuan Zhang. "KeyTitle: Towards Better Bug Report Title Generation by Keywords Planning". Software Quality Journal (2024).
    <span>[<a href="papers/SQJ24.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="EMSE22">[EMSE24]</td>
    <td valign="top">Bingting Chen, <b>Weiqin Zou*</b>, Biyu Cai, Qianshuang Meng, Wenjie Liu, Piji Li, Lin Chen. "An Empirical Study on the Potential of Word Embedding Techniques in Bug Report Management Tasks". Empirical Software Engineering (2024).
    <span>[<a href="papers/EMSE24.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="QRS24">[QRS24]</td>
    <td valign="top">Wenjie Liu, <b>Weiqin Zou*</b>, Bingting Chen, Biyu Cai, Jingxuan Zhang. "Query Quality Prediction for Text Retrieval-based Bug Localization." In 2024 IEEE 24th International Conference on Software Quality, Reliability and Security (QRS).
    <span>[<a href="papers/QRS24.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="IJSEKE24">[IJSEKE24]</td>
    <td valign="top">Xiaowei Zhang, Lin Chen, <b>Weiqin Zou</b>, Yulu Cao, Hao Ren, Zhi Wang, Yanhui Li, Yuming Zhou. "ICG: A Machine Learning Benchmark Dataset and Baselines for Inline Code Comments Generation Task." Int. J. Softw. Eng. Knowl. Eng. 34(2): 331-356 (2024).
    <span>[<a href="papers/IJSEKE24.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="JSJKX24">[JSJKX24]</td>
    <td valign="top">刘文杰, <b>邹卫琴*</b>, 蔡碧瑜, 陈冰婷. 基于主题一致性保持和伪相关反馈库扩展的缺陷报告重构方法[J/OL]. 计算机科学,1-15[2024-05-31].
    <span>[<a href="http://kns.cnki.net/kcms/detail/50.1075.tp.20231009.1653.049.html">HTML</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="TSE22">[TSE23]</td>
    <td valign="top">Xiaowei Zhang, <b>Weiqin Zou*</b>, Lin Chen*, Yanhui Li, Yuming Zhou. "Towards the Analysis and Completion of Syntactic Structure Ellipsis for Inline Comments." IEEE Transactions on Software Engineering. 49(4): 2285-2302 (2023).
    <span>[<a href="papers/TSE22.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="JoS21">[JoS21]</td>
    <td valign="top"><b>邹卫琴</b>, 张静宣, 张霄炜, 陈林, 玄跻峰, "缺陷报告质量研究综述." 软件学报. http://www.jos.org.cn/1000-9825/6500.htm.
    <span>[<a href="papers/JoS21.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="arXiv21">[arXiv21]</td>
    <td valign="top"><b>Weiqin Zou</b>, Enming Li, Chunrong Fang. "BLESER: Bug Localization Based on Enhanced Semantic Retrieval." arXiv preprint arXiv:2109.03555 (2021).
    <span>[<a href="papers/arXiv21.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="QRS21">[QRS21]</td>
    <td valign="top">Jiahui Liang, <b>Weiqin Zou</b>, Jingxuan Zhang, Zhiqiu Huang, Chenxing Sun, "A Deep Method Renaming Prediction and Refinement Approach for Java Projects." In 2021 IEEE 21th International Conference on Software Quality, Reliability and Security (QRS).
    <span>[<a href="papers/QRS21.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="APSEC21">[APSEC21]</td>
    <td valign="top">Jingxuan Zhang, <b>Weiqin Zou</b>, Zhiqiu Huang, "An Empirical Study on the Usage and Evolution of Identifier Styles in Practice." In 2021 Asia-Pacific Software Engineering Conference (APSEC).
    <span>[<a href="papers/APSEC21.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="QRS20">[QRS20]</td>
    <td valign="top">Ai Gong, Yi Zhong, <b>Weiqin Zou</b>, Yangyang Shi, and Chunrong Fang, "Incorporating Android Code Smells into Java Static Code Metrics for Security Risk Prediction of Android Applications." In 2020 IEEE 20th International Conference on Software Quality, Reliability and Security (QRS), pp. 30-40.
    <span>[<a href="papers/QRS20.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="TSE19">[TSE19]</td>
    <td valign="top"><b>Weiqin Zou</b>, David Lo, Pavneet Singh Kochhar, Xuan-Bach D. Le, Xin Xia, Yang Feng, Zhenyu Chen, and Baowen Xu, "Smart contract development: Challenges and opportunities." IEEE Transactions on Software Engineering (2019).
    <span>[<a href="papers/TSE19.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="arXiv19">[arXiv19]</td>
    <td valign="top">Haoran Wu, Xingya Wang, Jiehui Xu, <b>Weiqin Zou</b>, Lingming Zhang, and Zhenyu Chen. "Mutation testing for ethereum smart contract." arXiv preprint arXiv:1908.03707 (2019).
    <span>[<a href="papers/arXiv19.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="EMSE19">[EMSE19]</td>
    <td valign="top"><b>Weiqin Zou</b>, Jifeng Xuan, Xiaoyuan Xie, Zhenyu Chen, and Baowen Xu. "How does code style inconsistency affect pull request integration? An exploratory study on 117 GitHub projects." Empirical Software Engineering 24, no. 6 (2019): 3871-3903.
    <span>[<a href="papers/EMSE19.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="QRS19">[QRS19]</td>
    <td valign="top"><b>Weiqin Zou</b>, Weiqiang Zhang, Xin Xia, Reid Holmes, and Zhenyu Chen. "Branch Use in Practice: A Large-Scale Empirical Study of 2,923 Projects on GitHub." In 2019 IEEE 19th International Conference on Software Quality, Reliability and Security (QRS), pp. 306-317. IEEE, 2019.
    <span>[<a href="papers/QRS19.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="TSE18">[TSE18]</td>
    <td valign="top"><b> Weiqin Zou</b>, David Lo, Zhenyu Chen, Xin Xia, Yang Feng, and Baowen Xu. "How practitioners perceive automated bug report management techniques." IEEE Transactions on Software Engineering (2018).
    <span>[<a href="papers/TSE18.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="ICSME18">[ICSME18]</td>
    <td valign="top">Xin Zhang, Yang Chen, Yongfeng Gu, <b>Weiqin Zou</b>, Xiaoyuan Xie, Xiangyang Jia, and Jifeng Xuan. "How do multiple pull requests change the same code: A study of competing pull requests in github." In 2018 IEEE International Conference on Software Maintenance and Evolution (ICSME), pp. 228-239. IEEE, 2018.
    <span>[<a href="papers/ICSME18.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="APSEC18">[APSEC18]</td>
    <td valign="top">Lisha Li, Zhilei Ren, Xiaochen Li, <b>Weiqin Zou</b>, and He Jiang. "How are Issue Units Linked? Empirical Study on the Linking Behavior in GitHub." In 2018 25th Asia-Pacific Software Engineering Conference (APSEC), pp. 386-395. IEEE, 2018.
    <span>[<a href="papers/APSEC18.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="COMPSAC15">[COMPSAC15]</td>
    <td valign="top"><b>Weiqin Zou</b>, Xin Xia, Weiqiang Zhang, Zhenyu Chen, and David Lo. "An empirical study of bug fixing rate." In 2015 IEEE 39th Annual Computer Software and Applications Conference, vol. 2, pp. 254-263. IEEE, 2015.
    <span>[<a href="papers/COMPSAC15.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="TKDE15">[TKDE15]</td>
    <td valign="top">Jifeng Xuan, He Jiang, Yan Hu, Zhilei Ren, <b>Weiqin Zou</b>, Zhongxuan Luo, and Xindong Wu. "Towards effective bug triage with software data reduction techniques." IEEE transactions on knowledge and data engineering 27, no. 1 (2014): 264-280.
    <span>[<a href="papers/TKDE15.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="ICSE12">[ICSE12]</td>
    <td valign="top">Jifeng Xuan, He Jiang, Zhilei Ren, and <b>Weiqin Zou</b>. "Developer prioritization in bug repositories." In 2012 34th International Conference on Software Engineering (ICSE), pp. 25-35. IEEE, 2012.
    <span>[<a href="papers/ICSE12.pdf">Paper</a>]</span></td>
  </span></tr>

  <tr><span>
    <td valign="top" width="110" id="COMPSAC11">[COMPSAC11]</td>
    <td valign="top"><b>Weiqin Zou</b>, Yan Hu, Jifeng Xuan, and He Jiang. "Towards training set reduction for bug triage." In 2011 IEEE 35th Annual Computer Software and Applications Conference, pp. 576-581. IEEE, 2011.
    <span>[<a href="papers/COMPSAC11.pdf">Paper</a>]</span></td>
  </span></tr>
</table>



<span class='anchor' id='honors-and-awards'></span>
# 🏅 Honors and Awards

- *2018*, The program B for Outstanding PhD candidate, Nanjing University
- *2018*, Second-Class Scholarship, Nanjing University
- *2017*, Second-Class Scholarship, Nanjing University
- *2010*, Outstanding Graduate, Dalian University of Technology



<span class='anchor' id='academic-service'></span>
# 🏭 Academic Service

- Reviewer, TSE (IEEE Transactions on Software Engineering)
- Reviewer, IEEE Software
- Reviewer, JSS (Journal of Systems and Software)
- Reviewer, TR (IEEE Transactions on Reliability)
- Reviewer, ASE 2020 (The 35th IEEE/ACM International Conference on Automated Software Engineering)
- Reviewer, Internetware 2018 (The 10th Asia-Pacific Symposium on Internetware)
- Reviewer, ISSRE 2018 (The 29th IEEE International Symposium on Software Reliability Engineering)
- Reviewer, Internetware 2017 (The 9th Asia-Pacific Symposium on Internetware)
- PC member, DSA 2019 (International Workshop on Dependable Software and Applications)
- PC member, SATEI 2016 (Conference on Software Analysis, Testing and Evolution for Industry)
- PC member, TSA 2016 (The 3rd International Conference on Trustworthy Systems and Their Applications)



<span class='anchor' id='members'></span>
<link rel="stylesheet" type="text/css" href="assets/css/bootstrap.min.css">
<style>
  .image_box{
    width:150px;
    height:200px;
    display: inline-block;
    background-repeat: no-repeat;
    background-position: center center;
    background-origin: border-box;
    background-size: cover;
  }
</style>
# 🧑‍🎓 Members

## Class of 2021
<div class="bootstrap">
  <div class="row">
    <div class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
      <div class="image_box" style="background-image: url(/images/members/cbt.jpg);"></div>
      <div style="text-align: left;">
        <a href="https://cbting.github.io/" target="_blank">Bingting Chen/陈冰婷</a>
      </div>
    </div>
    <div class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
      <div class="image_box" style="background-image: url(/images/members/lwj2.jpg);"></div>
      <div style="text-align: left;">
        <a href="https://blue-lwj.github.io/" target="_blank">Wenjie Liu/刘文杰</a>
      </div>
    </div>
    <div class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
      <div class="image_box" style="background-image: url(/images/members/zwd.jpg);"></div>
      <div style="text-align: left;">
        <a href="https://anniewzd.github.io/" target="_blank">Zhaodan Wang/王昭丹</a>
      </div>
    </div>
  </div>
</div>

## Class of 2022
<div class="bootstrap">
  <div class="row">
    <div class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
      <div class="image_box" style="background-image: url(/images/members/cby.jpg);"></div>
      <div style="text-align: left;">
        <a href="https://caiby0927.github.io" target="_blank">Biyu Cai/蔡碧瑜</a>
      </div>
    </div>
    <div class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
      <div class="image_box" style="background-image: url(/images/members/cxh.jpg);"></div>
      <div style="text-align: left;">
        <a href="https://chenxiaohan0125.github.io" target="_blank">Xiaohan Chen/陈笑涵</a>
      </div>
    </div>
    <div class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
      <div class="image_box" style="background-image: url(/images/members/mqs.jpg);"></div>
      <div style="text-align: left;">
        <a href="https://mengqianshuang.github.io" target="_blank">Qianshuang Meng/孟千爽</a>
      </div>
    </div>
  </div>
</div>

## Class of 2023
<div class="bootstrap">
  <div class="row">
    <div class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
      <div class="image_box" style="background-image: url(/images/members/xh2.jpg);"></div>
      <div style="text-align: left;">
        <a href="https://lyraxv.github.io" target="_blank">Hui Xu/许慧</a>
      </div>
    </div>
    <div class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
      <div class="image_box" style="background-image: url(/images/members/zgw.png);"></div>
      <div style="text-align: left;">
        <a href="https://excuse2020.github.io/zgw.github.io/" target="_blank">Guowei Zhang/张国威</a>
      </div>
    </div>
  </div>
</div>

## Class of 2024
<div class="bootstrap">
  <div class="row">
    <div class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
      <div class="image_box" style="background-image: url(/images/members/wr.jpg);"></div>
      <div style="text-align: left;">
        Rui Wang/王瑞
      </div>
    </div>
    <div class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
      <div class="image_box" style="background-image: url(/images/members/wmj.jpg);"></div>
      <div style="text-align: left;">
        Mengjiao Wang/王梦娇
      </div>
    </div>
  </div>
</div>

## Class of 2025
<div class="bootstrap">
  <div class="row">
    <div class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
      <div class="image_box" style="background-image: url(/images/members/sby.jpg);"></div>
      <div style="text-align: left;">
        <a href="https://github.com/shinyashen" target="_blank">Boyang Shen/沈博洋</a>
      </div>
    </div>
  </div>
</div>



<span class='anchor' id='more-about-me'></span>
# 💬 More About Me

My hobbies are reading books (e.g., literature novels and history books), watching anime (mainly Japanese), swimming, travelling, etc.

I am always trying to figure out what I want, what life I want to lead, and still not getting the answer, haha.

Always on the way...
