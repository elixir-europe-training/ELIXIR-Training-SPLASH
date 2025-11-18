---
title: Resources
---

<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 g-4 mb-5 py-5">
    {% assign resource_pages = site.pages | where_exp: "page", "page.path contains 'pages/resources/'" | where_exp: "page", "page.id != nil" | where_exp: "page", "page.path != 'pages/resources/TEMPLATE_resource_page.md'" | sort: "title" %}
    
    {% for resource in resource_pages %}
    <div class="col">
        <a href="{{ resource.id }}" class="text-decoration-none">
            <div class="card h-100 resource-card shadow-sm">
                <div class="card-body d-flex flex-column">
                    <div class="resource-logo-container mb-3 text-center">
                        {% if resource.logo %}
                            <img src="assets/img/logos/{{ resource.logo }}" alt="{{ resource.title }} logo" class="resource-card-logo">
                        {% else %}
                            <img src="assets/img/icons/resource_icon.svg" alt="{{ resource.title }}" class="resource-card-icon">
                        {% endif %}
                    </div>
                    <h5 class="card-title text-center mb-3">{{ resource.title }}</h5>
                    
                    {% if resource.tags %}
                        <div class="resource-tags mb-3 text-center">
                            {% for tag_id in resource.tags %}
                                {% assign tag = site.data.resource_tags | where: "id", tag_id | first %}
                                {% if tag %}
                                    <span class="badge bg-{{ tag.color }} resource-tag" title="{{ tag.description }}">{{ tag.label }}</span>
                                {% endif %}
                            {% endfor %}
                        </div>
                    {% endif %}
                </div>
            </div>
        </a>
    </div>
    {% endfor %}
</div>



