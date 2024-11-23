from rest_framework import serializers
from library_app.models import Membership, Member, Book, Issuance, Collection, Category


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class IssuanceSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source='book_id.book_name', read_only=True)
    member_name = serializers.CharField(source='issuance_member.mem_name', read_only=True)
    member_phone = serializers.CharField(source='issuance_member.mem_phone', read_only=True)

    class Meta:
        model = Issuance
        fields = ['issuance_id', 'issuance_date', 'issued_by',
            'target_return_date', 'issuance_status',
            'book_name', 'member_name', 'member_phone']