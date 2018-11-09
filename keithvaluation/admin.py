from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import Site
from django.db import models
from django.utils.safestring import mark_safe

from keithvaluation import models as kv_models


class KVAdminSite(admin.AdminSite):
    site_header = "keithvaluation.com Administration"
    site_title = "Site Admin for keithvaluation.com"


kv_admin_site = KVAdminSite(name="kvadmin")


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        if value.url:
            img_tag = '<img src="%s"><br />' % value.url
        else:
            img_tag = ""
        return mark_safe(img_tag + super(AdminImageWidget, self).render(name, value, attrs))


class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "order")

    formfield_overrides = {models.ImageField: {"widget": AdminImageWidget}}


kv_admin_site.register(kv_models.Staff, StaffAdmin)


class ResearchAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "updated_date")


class REResearchAdmin(ResearchAdmin):
    list_display = ("title", "subtype", "description", "updated_date")
    list_filter = ("subtype",)


kv_admin_site.register(kv_models.REResearch, REResearchAdmin)


research_models = [
    kv_models.BVResearch,
    kv_models.EconomicTrend,
    kv_models.CourtCase,
    kv_models.Newsletter,
    kv_models.ExpertTestimony,
    kv_models.WhitePaper,
]
for rm in research_models:
    kv_admin_site.register(rm, ResearchAdmin)


class NewsAdmin(admin.ModelAdmin):
    def content_short(self, obj):
        post = "..." if len(obj.content) > 100 else ""
        return obj.content[:97] + post

    content_short.short_description = "Content"

    list_display = ("title", "content_short", "date")


kv_admin_site.register(kv_models.NewsItem, NewsAdmin)


class ExternalLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "description")


kv_admin_site.register(kv_models.ExternalLink, ExternalLinkAdmin)


class ImageInline(admin.TabularInline):
    model = kv_models.Image
    extra = 1


class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "property_name",
        "county",
        "available_to_hunt",
        "available_for_lease",
        "available_for_sale",
    )
    inlines = [ImageInline]
    prepopulated_fields = {"slug": ("property_name",)}


kv_admin_site.register(kv_models.Property, PropertyAdmin)


class BusinessListingAdmin(admin.ModelAdmin):
    list_display = ("business_name",)
    prepopulated_fields = {"slug": ("business_name",)}


kv_admin_site.register(kv_models.BusinessListing, BusinessListingAdmin)


class FeatureFlagAdmin(admin.ModelAdmin):
    list_display = ("name", "enabled")


kv_admin_site.register(kv_models.FeatureFlag, FeatureFlagAdmin)

kv_admin_site.register(User, UserAdmin)
kv_admin_site.register(Site)
