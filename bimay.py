try:
	import requests
	from bs4 import BeautifulSoup
	import datetime
except ImportError as e:
	print "There's import error for {} dependency".format(e)

login_url = "https://binusmaya.binus.ac.id/login/sys_login.php"
HEADER = {"Referer": "https://binusmaya.binus.ac.id/login/", "Origin": "https://binusmaya.binus.ac.index"}
BASE_URL = "https://binusmaya.binus.ac.id/services/ci/index.php/"
session_ = requests.session()

class bimay:
	
	# Method Description: Sign In Method
	# Parameter:
	#  - Username -> without @binus.ac.id
	#  - Password -> Password you use
	def sign_in(self, username, password):
		sign = session_.post(login_url, headers=HEADER, data= {'uid': username,'pass': password})
		# Check for error message using beautiful soup
		# any other suggestions?
		check_error = BeautifulSoup(sign.content, 'html.parser')
		error_message = check_error.find_all('div', {'id': 'login_error'})
		if not error_message:
			return True
		return False

	# Method Description: Get Profile Method
	# Return: User Profile
	# Return Data Type: Lists
	def get_profile(self):
		profile = session_.get(BASE_URL + "student/profile/profileStudent", headers=HEADER, cookies=session_.cookies).json()
		return profile

	# Method Description: Get Student Activity Transcript (SAT) Score Method
	# Return: User SAT Score 
	# Return Data Type: Lists
	def get_sat(self):
		sat = session_.post(BASE_URL + "sat/studentactivitytranscript/GetStudentActivityPoint", headers=HEADER, cookies=session_.cookies).json()
		return sat

	# Method Description: Get Community Services Score Method
	# Return: User Community Services Score
	# Return Data Type: List
	def get_community_services(self):
		community_services = session_.post(BASE_URL + "sat/studentactivitytranscript/GetStudentActivityPoint", headers=HEADER, cookies=session_.cookies).json()
		return community_services

	# Method Description: Get Financial Information
	# Return: User Financial Informations
	# Return Data Type: List
	def get_financial_information(self):
		financial_information = session_.get(BASE_URL + "finacial/virtualaccount", headers=HEADER, cookies=session_.cookies).json()
		financial_summary = session_.get(BASE_URL + "financial/getFinancialSummary", headers=HEADER, cookies=session_.cookies).json()
		return ""

	# Method Description: Get Forum Information
	# Return: User Forums Informations
	# Return Data Type: List
	def get_forum_information(self):
		degree = session_.post(BASE_URL + "/forum/getAcadCareer", headers=HEADER, cookies=session_.cookies).json()
		period = session_.post(BASE_URL + "/forum/getPeriod", headers=HEADER, cookies=session_.cookies).json()
		course = session_.post(BASE_URL + "/forum/getCourse", headers=HEADER, cookies=session_.cookies).json()
		class_ = session_.post(BASE_URL + "/forum/getClass", headers=HEADER, cookies=session_.cookies).json()
		topic = session_.post(BASE_URL + "/forum/getTopic", headers=HEADER, cookies=session_.cookies).json()
		access_type_id = session_.post(BASE_URL + "/forum/getAccessTypeID", headers=HEADER, cookies=session_.cookies).json()
		learning_outcomes = session_.post(BASE_URL + "/student/classes/getLearningOutcomes/", headers=HEADER, cookies=session_.cookies).json()
		return ""

	# Method Description: Get Forum Message
	# Return: User Forums Message
	# Return Data Type: List
	def send_forum_message(self):
		return ""

	# Method Description: Get Detailed Forum Information
	# Return: User Detailed Forums Informations
	# Return Data Type: List
	def get_detailed_forum_information(self):
		return ""

	# Method Description: Get Course Information
	# Return: User Course Informations
	# Return Data Type: List
	def get_course_information(self):
		course_information = session_.get(BASE_URL + "student/init/getCourses", headers=HEADER, cookies=session_.cookies).json()
		return course_information

	# Method Description: Get Course Material
	# Return: User Course Material
	# Return Data Type: List
	def get_course_material(self,courseId, crseId, term, ssrComponent, classNumber):
		material_url_format = "student/classes/resources/{}/{}/{}/{}/{}".format(courseId, crseId, term, ssrComponent, classNumber)
		course_material = session_.get(BASE_URL + material_url_format, headers=HEADER, cookies=session_.cookies).json()
		return course_material

	# Method Description: Get Forum Information
	# Return: User Forums Informations
	# Return Data Type: List
	def get_course_assignment(self,courseId, crseId, term, ssrComponent, classNumber):
		material_url_format = "student/classes/assignmentType/{}/{}/{}/{}/{}/01".format(courseId, crseId, term, ssrComponent, classNumber)
		course_assignment = session_.get(BASE_URL + material_url_format, headers=HEADER, cookies=session_.cookies).json()
		return course_assignment

	# Method Description: Get Exam Score
	# Return: User Exam Score
	# Return Data Type: List
	def get_exam_score(self,terms):
		exam_score = session_.post(BASE_URL + "scoring/ViewGrade/getStudentScore/" + terms, headers=HEADER, cookies=session_.cookies).json()	
		return exam_score

	# Method Description: Get Exam Schedule
	# Return: User Exam Schedule
	# Return Data Type: List
	def get_exam_schedule(self, exam_request_body):
		exam_schedule = session_.post(BASE_URL + "newExam/Schedule/getOwnScheduleStudent", headers=HEADER, cookies=session_.cookies, data={exam_request_body})
		return exam_schedule

	# Method Description: Get Forum Information
	# Return: User Forums Informations
	# Return Data Type: List
	def get_schedule(self):
		schedule = session_.get(BASE_URL + "student/class_schedule/classScheduleGetStudentClassSchedule", headers=HEADER, cookies=session_.cookies).json()
		return schedule

	# Method Description: Get News Information
	# Return: User News Information
	# Return Data Type: List
	def get_news(self):
		news = session_.post(BASE_URL + "student/news/getAllNewsDashboard/", headers=HEADER, cookies=session_.cookies).json()
		return news

	# Method Description: Get Academic Advisory Information
	# Return: User Academic Advisory Informations
	# Return Data Type: List
	def get_academic_advisory(self):
		academic_advisory = session_.post(BASE_URL + "academicAdvisory/studentAcademicAdvisory/getPeriod", headers=HEADER, cookies=session_.cookies).json()
		return academic_advisory

	# Method Description: Get Message Information
	# Return: User Message Informations
	# Return Data Type: List
	def get_message(self):
		message = session_.post(BASE_URL + "message/getinboxdata", headers=HEADER, cookies=session_.cookies).json()
		return message

	# Method Description: Get Feedback Information
	# Return: User Feedback Informations
	# Return Data Type: List
	def get_feedback(self):
		feedback = session_.post(BASE_URL + "student/feedback/get_feedback/get", headers=HEADER, cookies=session_.cookies).json()
		return feedback

	# Method Description: Get Letter Request Information
	# Return: User Letter Request Informations
	# Return Data Type: List
	def send_letter_request(self):
		return ""

	# Method Description: Get Letter Request History Information
	# Return: User Letter Request History Informations
	# Return Data Type: List
	def get_letter_request_history(self):
		letter_request_history = session_.post(BASE_URL + "student/support/getLetterHistory", headers=HEADER, cookies=session_.cookies).json()
		return letter_request_history

	# Method Description: Get Current Terms Information
	# Return: User Current Terms Informations
	# Return Data Type: List
	def get_current_terms(self):
		current_terms = session_.post("https://binusmaya.binus.ac.id/services/ci/index.php/scoring/ViewGrade/getPeriodByBinusianId", headers=HEADER, cookies=session_.cookies).json()
		return current_terms

	# Method Description: Get User Sessions Information
	# Return: User Sessions Informations
	# Return Data Type: List
	def check_session(self):
		login_session = session_.get("https://binusmaya.binus.ac.id/services/ci/index.php/staff/init/check_session", headers=HEADER, cookies=session_.cookies).json()
		return login_session

