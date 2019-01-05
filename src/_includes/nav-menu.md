{% capture nav_bar %}
* [Home]({{ site.baseurl }}/)
* [Blog]({{ site.baseurl }}/blog)
* [Bored]({{ site.baseurl }}/bored)
* [Resources]({{ site.baseurl }}/resources)
{% endcapture %}
{{ nav_bar | markdownify }}
