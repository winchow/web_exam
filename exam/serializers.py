from exam.models import Lac,Subject
from rest_framework import serializers

class LacSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lac
		fields = ('name','job_position','department','campus','type','ict_id')
		#fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = ('ExamT','InstrucT','DegreeT','ratio','student','Sid','T_type','S_type','Degree','Examiner','SectionT')
		#fields = '__all__'