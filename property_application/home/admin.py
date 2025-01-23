from django.contrib import admin

# Register your models here.

from.models import MasterState,CityMaster,CustomerType , PropertyType ,Location , ReferenceMaster



class StateAdmin(admin.ModelAdmin):
    model = MasterState
    list_display =('__str__','state_name')
    search_fields = ('state_name',)
    
    # Add filters on the admin page for better navigation
    list_filter = ('state_name',)

    # Allow the admin to view more fields when editing
    fieldsets = (
        (None, {
            'fields': ('state_name',)  # Customize the fields shown in the edit form
        }),
    )
admin.site.register(MasterState,StateAdmin)


class CityAdmin(admin.ModelAdmin):
    model = CityMaster
    list_display = ('__str__', 'city_name', 'get_state_name')  # Display state name in list view

    # Add custom method to fetch state name
    def get_state_name(self, obj):
        return obj.state.state_name if obj.state else "Unknown"  # Use 'state' field here
    
    get_state_name.short_description = 'State Name'  # Sets the column header in the list view

    search_fields = ('city_name', 'state__state_name')  # Search by state name

    # Add filters on the admin page for better navigation
    list_filter = ('city_name', 'state')

    # Allow the admin to view more fields when editing
    fieldsets = (
        (None, {
            'fields': ('city_name', 'state')  # Customize the fields shown in the edit form
        }),
    )

admin.site.register(CityMaster, CityAdmin)


class CustomerTypeAdmin(admin.ModelAdmin):
    model = CustomerType
    list_display =('__str__','type_name')
    search_fields = ('type_name',)
    
    # Add filters on the admin page for better navigation
    list_filter = ('type_name',)

    # Allow the admin to view more fields when editing
    fieldsets = (
        (None, {
            'fields': ('type_name',)  # Customize the fields shown in the edit form
        }),
    )
admin.site.register(CustomerType, CustomerTypeAdmin)


class PropertyTypeAdmin(admin.ModelAdmin):
    model = PropertyType
    list_display =('__str__','property_type_name')
    search_fields = ('property_type_name',)
    
    # Add filters on the admin page for better navigation
    list_filter = ('property_type_name',)

    # Allow the admin to view more fields when editing
    fieldsets = (
        (None, {
            'fields': ('property_type_name',)  # Customize the fields shown in the edit form
        }),
    )
admin.site.register(PropertyType,PropertyTypeAdmin)




class LOcationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ('__str__', 'location_name', 'get_city_name')  # Display state name in list view

    # Add custom method to fetch state name
    def get_city_name(self, obj):
        return obj.city.city_name if obj.city else "Unknown"  # Use 'state' field here
    
    get_city_name.short_description = 'City Name'  # Sets the column header in the list view

    search_fields = ('location_name', 'city__city_name')  # Search by state name

    # Add filters on the admin page for better navigation
    list_filter = ('location_name', 'city')

    # Allow the admin to view more fields when editing
    fieldsets = (
        (None, {
            'fields': ('location_name', 'city')  # Customize the fields shown in the edit form
        }),
    )

admin.site.register(Location, LOcationAdmin)



class ReferenceAdmin(admin.ModelAdmin):
    model = ReferenceMaster
    list_display =('__str__','reference_name')
    search_fields = ('reference_name',)
    
    # Add filters on the admin page for better navigation
    list_filter = ('reference_name',)

    # Allow the admin to view more fields when editing
    fieldsets = (
        (None, {
            'fields': ('reference_name',)  # Customize the fields shown in the edit form
        }),
    )
admin.site.register(ReferenceMaster,ReferenceAdmin)