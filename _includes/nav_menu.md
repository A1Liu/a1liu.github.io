{% capture nav_bar %}
* [Home]({{ site.baseurl }}/)
* [About]({{ site.baseurl }}/about)
* [Projects]({{ site.baseurl }}/projects)
* [Bored]({{ site.baseurl }}/bored)
* [Resources]({{ site.baseurl }}/resources)
{% endcapture %}
{{ nav_bar | markdownify }}
