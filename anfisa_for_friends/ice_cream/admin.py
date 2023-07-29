from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category, Topping, Wrapper, IceCream

# Этот вариант сработает для всех моделей приложения.
# Вместо пустого значения в админке будет отображена строка "Не задано".
admin.site.empty_value_display = 'Не задано'

# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',        
    )

# Создаём класс, в котором будем описывать настройки админки:
class IceCreamAdmin(admin.ModelAdmin):
    # В этом классе опишем все настройки, какие захотим.
    list_display = (
        'title',
        'price',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
        'output_order'
    )
    list_editable = (
        'price',
        'is_published',
        'is_on_main',
        'category',
        'output_order'
    )    
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)

    # Это свойство сработает для всех полей этой модели.
    # Вместо пустого значения будет выводиться строка "Не задано".
    empty_value_display = 'Не задано'

    # Указываем, для каких связанных моделей нужно включить такой интерфейс:
    filter_horizontal = ('toppings',)


# Регистрируем класс с настройками админки для моделей IceCream и Category:
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
# Регистрируем модели Topping и Wrapper, 
# чтобы ими можно было управлять через админку
# (интерфейс админки для этих моделей останется стандартным):
admin.site.register(Topping)
admin.site.register(Wrapper) 