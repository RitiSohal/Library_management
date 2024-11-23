from django.db.models import Count
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Book, Issuance, Member


@api_view(['GET'])
@permission_classes([AllowAny])
def books_never_borrowed(request):
    books = Book.objects.filter(issuance__isnull=True)
    data = [{'book_name': book.book_name, 'author': book.book_publisher} for book in books]
    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def outstanding_books(request):
    outstanding_books = Issuance.objects.filter(issuance_status='outstanding')
    data = [
        {
            'member_name': issuance.issuance_member.mem_name,
            'book_name': issuance.book.book_name,
            'issued_date': issuance.issuance_date,
            'target_return_date': issuance.target_return_date,
            'author': issuance.book.book_publisher
        }
        for issuance in outstanding_books
    ]
    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def top_borrowed_books(request):
    top_books = Issuance.objects.values('book__book_name').annotate(
        times_borrowed=Count('id'),
        unique_members=Count('issuance_member', distinct=True)
    ).order_by('-times_borrowed')[:10]
    data = [{'book_name': book['book__book_name'], 'times_borrowed': book['times_borrowed'],
             'unique_members': book['unique_members']} for book in top_books]
    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def top_member(request):
    top_member = Issuance.objects.values('issuance_member__mem_name').annotate(
        books_borrowed=Count('book')
    ).order_by('-books_borrowed').first()
    data = {
        'member_name': top_member['issuance_member__mem_name'],
        'books_borrowed': top_member['books_borrowed']
    }
    return Response(data)