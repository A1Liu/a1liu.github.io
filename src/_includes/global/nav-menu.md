{% capture nav_bar %}
[Home]({{ site.baseurl }}/)
[Blog]({{ site.baseurl }}/blog/)
[CV]({{ site.baseurl }}/career/)
[Resources]({{ site.baseurl }}/resources/)
{% endcapture %}
{{ nav_bar | markdownify }}
