from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library_app.views import MembershipViewSet, CategoryViewSet, MemberViewSet, BookViewSet, IssuanceViewSet, pending_returns_dashboard, CollectionViewSet
from library_app.custom_views import books_never_borrowed, outstanding_books, top_borrowed_books, top_member

router = DefaultRouter()
router.register(r'membership', MembershipViewSet)
router.register(r'member', MemberViewSet)
router.register(r'book', BookViewSet)
router.register(r'issuance', IssuanceViewSet)
router.register(r'collection', CollectionViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/dashboard/', pending_returns_dashboard, name='pending_returns_dashboard'),
    path('api/book/never-borrowed/', books_never_borrowed, name='books_never_borrowed'),
    path('book/outstanding/', outstanding_books, name='outstanding_books'),
    path('book/top-borrowed/', top_borrowed_books, name='top_borrowed_books'),
    path('member/top/', top_member, name='top_member'),
]
