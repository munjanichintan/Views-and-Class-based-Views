from django.shortcuts import render
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class StudentAPI(APIView):
	def get(self, request, id=None, format=None):
		if request.method == 'GET':
			if id is not None:
				stu = Student.objects.get(id=id)
				serializer = StudentSerializer(stu)
				return Response(serializer.data)
			stu = Student.objects.all()
			serializer = StudentSerializer(stu, many=True)
			return Response(serializer.data)

	def post(self, request, id=None, format=None):
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			res = {'msg': 'Data Created Successfully'}
			return Response(res, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, id=None, format=None):
		stu = Student.objects.get(id=id)
		serializer = StudentSerializer(stu, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg': 'Complete Data Updated Successfully'})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def patch(self, request, id=None, format=None):
		stu = Student.objects.get(id=id)
		serializer = StudentSerializer(stu, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg': 'Partial Data Updated Successfully'})
		return Response(serializer.errors)

	def delete(self, request, id=None, format=None):
		stu = Student.objects.get(id=id)
		stu.delete()
		return Response({'msg': {'Data Deleted Successfully'}})



@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, id=None):
	if request.method == 'GET':
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			return Response(serializer.data)
		stu = Student.objects.all()
		serializer = StudentSerializer(stu, many=True)
		return Response(serializer.data)

	if request.method == 'POST':
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			res = {'msg': 'Data Created Successfully'}
			return Response(res, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'PUT':
		stu = Student.objects.get(id=id)
		serializer = StudentSerializer(stu, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg': 'Complete Data Updated Successfully'})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'PATCH':
		stu = Student.objects.get(id=id)
		serializer = StudentSerializer(stu, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg': 'Partial Data Updated Successfully'})
		return Response(serializer.errors)

	if request.method == 'DELETE':
		stu = Student.objects.get(id=id)
		stu.delete()
		return Response({'msg': {'Data Deleted Successfully'}})