---
title: "{{title}}"
Authors: "{{authors}}"
date: '{{date | format("YYYY-MM-DD")}}'
updated: "{{dateModified | format(“YYYY-MM-DD”)}}"
Link: "{{url}}"
tags:
  {% if tags.length > 0 -%}
    {%- for t in tags -%}
      {%- set replaced_tag = t.tag %}
      {%- set replaced_tag = replaced_tag | replace(" ", "-") -%}
      {{ "\n - " ~ replaced_tag }}
    {%- endfor %}
  {%- endif %}
---
> [!Abstract]
> {%- if abstractNote %}
> {{abstractNote}}
> {%- endif -%}

{%- if annotations.length %}\
## 1. Annotations
{%- endif %}


{%- macro calloutHeader(type, color) -%}  
{%- if type == "highlight" -%}  
<mark style="background-color: {{color}}">Highlight</mark>  
{%- endif -%}

{%- if type == "text" -%}  
Note  
{%- endif -%}  
{%- endmacro -%}

{%- set annots = annotations | filterby("date", "dateafter", lastExportDate) -%}  
{%- if annots.length > 0 %}  
{% for annot in annots -%}  
> {{calloutHeader(annot.type, annot.color)}}  
{%- if annot.annotatedText %}  
> {{annot.annotatedText | nl2br}}  
{%- endif -%}  
{%- if annot.imageRelativePath %}  
> ![[{{annot.imageRelativePath}}]]  
{%- endif %}  
> [page {{ annot.page if annot.page else 1 }}]({{annot.desktopURI | replace(" ", "%20")}})
{%- if annot.comment %}  
> - {{annot.comment | nl2br}}  
{% endif %}

{% endfor -%}  
{% endif -%}