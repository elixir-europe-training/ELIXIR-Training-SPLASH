---
title: Resources
sidebar: false
---

<!-- Search and Filter Section -->
<div class="row mb-4">
    <div class="col-lg-4 col-xl-3 mb-3">
        <div class="sticky-top" style="top: 6rem;">
            <input type="text" id="resourceSearch" class="form-control mb-3" placeholder="Search resources...">
            <div id="tagFilters">
                <div class="mb-3">
                    <button class="btn btn-sm btn-outline-secondary active filter-tag w-100" data-filter="all">All Resources</button>
                </div>
                
                {% assign all_tags = "" | split: "" %}
                {% for page in site.pages %}
                    {% if page.path contains 'pages/resources/' and page.id and page.tags %}
                        {% for tag_id in page.tags %}
                            {% unless all_tags contains tag_id %}
                                {% assign all_tags = all_tags | push: tag_id %}
                            {% endunless %}
                        {% endfor %}
                    {% endif %}
                {% endfor %}
                
                {% for category_info in site.data.tag_categories %}
                    {% assign category_has_tags = false %}
                    {% assign category_tags_html = "" %}
                    
                    {% comment %}Iterate through resource_tags in order to preserve sequence{% endcomment %}
                    {% for tag in site.data.resource_tags %}
                        {% if tag.category == category_info.id and all_tags contains tag.id %}
                            {% assign category_has_tags = true %}
                            {% capture tag_button %}
                                <button class="btn btn-sm btn-outline-{{ tag.color }} filter-tag" data-filter="{{ tag.id }}" title="{{ tag.description }}">
                                    {{ tag.label }}
                                </button>
                            {% endcapture %}
                            {% assign category_tags_html = category_tags_html | append: tag_button %}
                        {% endif %}
                    {% endfor %}
                    
                    {% if category_has_tags %}
                        <div class="tag-category-group mb-3">
                            <div class="tag-category-label text-muted text-uppercase small fw-bold mb-2">
                                {{ category_info.label }}
                                {% if category_info.description %}
                                    <i class="fas fa-info-circle ms-1" title="{{ category_info.description }}" data-bs-toggle="tooltip" data-bs-placement="right"></i>
                                {% endif %}
                            </div>
                            <div class="d-flex flex-wrap gap-2">
                                {{ category_tags_html }}
                            </div>
                        </div>
                    {% endif %}
                {% endfor %}
            </div>
        </div>
    </div>
    
    <div class="col-lg-8 col-xl-9">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 row-cols-xl-4 g-3 mb-5" id="resourceGrid">
            {% assign resource_pages = site.pages | where_exp: "page", "page.path contains 'pages/resources/'" | where_exp: "page", "page.id != nil" | where_exp: "page", "page.path != 'pages/resources/TEMPLATE_resource_page.md'" | sort: "title" %}
            
            {% for resource in resource_pages %}
            <div class="col resource-item" data-tags="{% if resource.tags %}{% for tag in resource.tags %}{{ tag }} {% endfor %}{% endif %}" data-title="{{ resource.title | downcase }}">
                <a href="{{ resource.id }}" class="text-decoration-none">
                    <div class="card h-100 resource-card shadow-sm">
                        <div class="card-body d-flex flex-column">
                            <div class="resource-logo-container mb-2 text-center">
                                {% if resource.logo %}
                                    <img src="assets/img/logos/{{ resource.logo }}" alt="{{ resource.title }} logo" class="resource-card-logo">
                                {% else %}
                                    <img src="assets/img/icons/resource_icon.svg" alt="{{ resource.title }}" class="resource-card-icon">
                                {% endif %}
                            </div>
                            <h5 class="card-title text-center mb-2">{{ resource.title }}</h5>
                            
                            {% if resource.tags %}
                                <div class="resource-tags mb-2 text-center">
                                    {% for tag_id in resource.tags %}
                                        {% assign tag = site.data.resource_tags | where: "id", tag_id | first %}
                                        {% if tag %}
                                            <span class="badge bg-{{ tag.color }} resource-tag" data-tag="{{ tag_id }}" title="{{ tag.description }}">{{ tag.label }}</span>
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

        <div id="noResults" class="text-center py-5 d-none">
            <p class="text-muted fs-5">No resources found matching your search.</p>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('resourceSearch');
    const filterButtons = document.querySelectorAll('.filter-tag');
    const resourceItems = document.querySelectorAll('.resource-item');
    const noResults = document.getElementById('noResults');
    const resourceGrid = document.getElementById('resourceGrid');
    
    let activeFilter = 'all';
    
    // Filter function
    function filterResources() {
        const searchTerm = searchInput.value.toLowerCase();
        let visibleCount = 0;
        
        resourceItems.forEach(item => {
            const title = item.dataset.title;
            const tags = item.dataset.tags;
            
            // Check if matches search term
            const matchesSearch = title.includes(searchTerm) || tags.toLowerCase().includes(searchTerm);
            
            // Check if matches active filter
            const matchesFilter = activeFilter === 'all' || tags.includes(activeFilter);
            
            // Show/hide based on both conditions
            if (matchesSearch && matchesFilter) {
                item.style.display = '';
                visibleCount++;
            } else {
                item.style.display = 'none';
            }
        });
        
        // Show/hide no results message
        if (visibleCount === 0) {
            resourceGrid.classList.add('d-none');
            noResults.classList.remove('d-none');
        } else {
            resourceGrid.classList.remove('d-none');
            noResults.classList.add('d-none');
        }
    }
    
    // Search input handler
    searchInput.addEventListener('input', filterResources);
    
    // Filter button handlers
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // If clicking the already active filter (except "all"), deselect it and go back to "all"
            if (this.dataset.filter === activeFilter && activeFilter !== 'all') {
                activeFilter = 'all';
                filterButtons.forEach(btn => btn.classList.remove('active'));
                document.querySelector('.filter-tag[data-filter="all"]').classList.add('active');
            } else {
                // Update active filter
                activeFilter = this.dataset.filter;
                
                // Update button states
                filterButtons.forEach(btn => btn.classList.remove('active'));
                this.classList.add('active');
            }
            
            // Apply filter
            filterResources();
        });
    });
    
    // Make tag badges clickable to filter
    document.querySelectorAll('.resource-tag').forEach(badge => {
        badge.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const tagId = this.dataset.tag;
            const filterButton = document.querySelector(`.filter-tag[data-filter="${tagId}"]`);
            
            if (filterButton) {
                filterButton.click();
                // Scroll to top to show filters
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        });
    });
    
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
});
</script>
