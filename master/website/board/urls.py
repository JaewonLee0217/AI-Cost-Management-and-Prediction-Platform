from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    # 화면 urls 항목
    path('', views.home, name='home'),
    path('b_bizarea/', views.b_bizarea, name='b_bizarea_list'),
    path('b_bizpartner/', views.b_bizpartner, name='b_bizpartner_list'),
    path('b_bizunit/', views.b_bizunit, name='b_bizunit_list'),
    path('b_co/', views.b_co, name='b_co_list'),
    path('b_factory/', views.b_factory, name='b_factory_list'),
    path('b_item/', views.b_item, name='b_item_list'),
    path('b_user/', views.b_user, name='b_user_list'),
    path('b_workcenter/', views.b_workcenter, name='b_workcenter_list'),
    path('b_bom/', views.b_bom, name='b_bom_list'),
    path('cb_code_hdr/', views.cb_code_hdr, name='cb_code_hdr_list'),
    path('cb_cost_center/', views.cb_cost_center, name='cb_cost_center_list'),
    path('codemanage/', views.codemanage, name='codemanage'),
    path('b_itemaccnt/', views.b_itemaccnt, name='b_itemaccnt'),
    path('b_itemgrp/', views.b_itemgrp, name='b_itemgrp'),

    # 사용자 관리
    path('member_register', views.member_register, name="member_register"),
    path('member_id_check', views.member_id_check, name="member_id_check"),
    path('member_insert', views.member_insert, name="member_insert"),
    path('member_login', views.member_login, name="member_login"),
    path('member_logout', views.member_logout, name="member_logout"),

    # 사업장
    path('b_bizarea/bizarea_element_insert', views.bizarea_element_insert, name="bizarea_element_insert"),
    path('b_bizarea/bizarea_element_update', views.bizarea_element_update, name="bizarea_element_update"),
    path('b_bizarea/bizarea_element_delete', views.bizarea_element_delete, name="bizarea_element_delete"),
    # 사업부
    path('b_bizunit/bizunit_element_insert', views.bizunit_element_insert, name="bizunit_element_insert"),
    path('b_bizunit/bizunit_element_update', views.bizunit_element_update, name="bizunit_element_update"),
    path('b_bizunit/bizunit_element_delete', views.bizunit_element_delete, name="bizunit_element_delete"),

    # 공장 기능 항목
    path('b_factory/factory_element_insert', views.factory_element_insert, name="factory_element_insert"),
    path('b_factory/factory_element_update', views.factory_element_update, name="factory_element_update"),
    path('b_factory/factory_element_delete', views.factory_element_delete, name="factory_element_delete"),

    # 거래처 기능 항목
    path('b_bizpartner/bizpartner_element_insert', views.bizpartner_element_insert, name="bizpartner_element_insert"),
    path('b_bizpartner/bizpartner_element_update', views.bizpartner_element_update, name="bizpartner_element_update"),
    path('b_bizpartner/bizpartner_element_delete', views.bizpartner_element_delete, name="bizpartner_element_delete"),

    # 통합코드 헤더 기능 항목
    path('codemanage/codetype_insert', views.codetype_insert, name="codetype_insert"),
    path('codemanage/codetype_update', views.codetype_update, name="codetype_update"),
    path('codemanage/codetype_delete', views.codetype_delete, name="codetype_delete"),

    # 통합코드 디테일 기능 항목
    path('codemanage/code_insert', views.code_insert, name='code_insert'),
    path('codemanage/code_update', views.code_update, name='code_update'),
    path('codemanage/code_delete', views.code_delete, name='code_delete'),
    path('codemanage/code_view', views.code_view, name='code_view'),

    # 품목계정 기능 항목
    path('b_itemaccnt/itemaccnt_insert', views.itemaccnt_insert, name='itemaccnt_insert'),
    path('b_itemaccnt/itemaccnt_delete', views.itemaccnt_delete, name='itemaccnt_delete'),

    # 품목그룹 기능 항목
    path('b_itemgrp/itemgrp_insert', views.itemgrp_insert, name='itemgrp_insert'),
    path('b_itemgrp/itemgrp_delete', views.itemgrp_delete, name='itemgrp_delete'),

    # 품목마스터 기능 항목
    path('b_item/item_insert', views.item_insert, name='item_insert'),
    path('b_item/item_update', views.item_update, name='item_update'),
    path('b_item/item_delete', views.item_delete, name='item_delete'),

    #BOM 기능 항목
    path('b_bom/bom_create', views.bom_create, name="bom_create"),
    path('b_bom/bomitem_read', views.bomitem_read, name="bomitem_read"),
    path('b_bom/bomitem_pick', views.bomitem_pick, name="bomitem_pick"),
    path('b_bom/bom_update', views.bom_update, name="bom_update"),
]
