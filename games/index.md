---
layout: default
---

## Welcome
Hi there, welcome to a space for thoughts about all sorts of games. For now,
there's not much here, but I hope you'll come and visit now and then.

If you want to learn more about me, check out my main blog at
[phizzle.space][phizzle] where I write about programming and other topics.

#### Recent Posts
{% for post in site.posts %}
<a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
{% endfor %}

***

[phizzle]: http://phizzle.space
