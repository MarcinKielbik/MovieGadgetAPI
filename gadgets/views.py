from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from gadgets.models import MovieGadget
from gadgets.serializers import MovieGadgetSerializer


@api_view(['GET', 'POST'])
def gadget_list(request):
    if request.method == 'GET':
        gadgets = MovieGadget.objects.all()
        serializer = MovieGadgetSerializer(gadgets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieGadgetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def gadget_detail(request, gadget_id):
    gadget = get_object_or_404(MovieGadget, pk=gadget_id)

    if request.method == 'GET':
        serializer = MovieGadgetSerializer(gadget)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieGadgetSerializer(
            gadget,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'PATCH':
        serializer = MovieGadgetSerializer(
            gadget,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        gadget.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )