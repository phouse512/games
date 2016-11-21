---
layout: default
---

## About
Welcome to sports analysis

{% for post in site.posts %}
    <h2> {{post.title}}</h2>
    <a href="{{ post.url | prepend: site.baseurl }}">Linky</a>
{% endfor %}

This is a [link](http://google.com). Something *italics* and something **bold**.


---

Here is a blockquote

> To a great mind, nothing is little

## References

* Foo Bar: Head of Department, Placeholder Names, Lorem
* John Doe: Associate Professor, Department of Computer Science, Ipsum
