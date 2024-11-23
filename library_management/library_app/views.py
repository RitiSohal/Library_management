from django.shortcuts import render
from rest_framework import viewsets
from library_app.serializers import BookSerializer, IssuanceSerializer, CollectionSerializer
from library_app.models import *
from library_app.serializers import MembershipSerializer, MemberSerializer, CategorySerializer


# Create your views here.
class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class IssuanceViewSet(viewsets.ModelViewSet):
    queryset = Issuance.objects.all()
    serializer_class = IssuanceSerializer


def pending_returns_dashboard(request):
    outstanding_books = Issuance.objects.filter(issuance_status='outstanding')
    records = [
        {
            'member_name': issuance.issuance_member.mem_name,
            'book_name': issuance.book_id.book_name,
            'issued_date': issuance.issuance_date,
            'target_return_date': issuance.target_return_date,
            'author': issuance.book_id.book_publisher
        }
        for issuance in outstanding_books
    ]
    return render(request, 'dashboard.html', {'records': records})






# Create your views here.
