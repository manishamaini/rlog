from django.db import models

# Create your models here.
class staging_records(models.Model):
	sr_no = models.IntegerField(auto_now_add = True, unique_key = True)
	recruiter = models.CharField(foriegn_key = True)
	client = models.CharField(foriegn_key = True)
	position = models.AlphaNumericField()
	reqt_date = models.DateField()
	date_cv_submitted = models.DateField()
	candidate_name = models.CharField()
	current_status = models.IntegerField()
	current_status_desc = models.CharField()
	interview_date = models.DateField()
	remarks = models.CharField()
	skills = models.CharField()
	current_org = models.CharField()
	qualification = models.CharField()
	total_exp = models.FloatField()
	current_location = models.CharField()
	contact_details_mobile = models.IntegerField(max_len = 10, unique_key = True)
	contact_details_mobile = models.IntegerField(max_len = 10, unique_key = True)
	email = models.CharField()
    expected_salary_percentage = models.IntegerField()
    expected_salary_amt = models.FloatField()
    notice_period = models.IntegerField()
    Int_Tele_date = models.DateField()
    Int_Tele_result = models.CharField()
    Int_P1_date = models.DateField()
    Int_P1_result = models.CharField()
    Int_p2_date = models.DateField()
    Int_p2_result = models.Charfield()
    Int_p3_date = models.DateField()
    Int_p3_result = models.Charfield()
    Int_Final_date = models.DateField()
    Int_Final_result = models.Charfield()
    Int_HR_date = models.DateField()
    Int_HR_result = models.Charfield()
    offer_date = models.DateField()
    offer_amt = models.FloatField()
    joining_date = models.DateField()
    vacancy_code = models.Charfield()
    applicant_code = models.Charfield()
    DOB = models.DateField()
    preffered_company = models.Charfield()
    preffered_location = models.Charfield()
    week_number = models.IntegerField()
    wk_year = models.IntegerField()
    reason = models.Charfield()

class good_records(models.Model):
	sr_no = models.IntegerField(auto_now_add = True, unique_key = True)
	recruiter = models.CharField(foriegn_key = True)
	client = models.CharField(foriegn_key = True)
	position = models.AlphaNumericField()
	reqt_date = models.DateField()
	date_cv_submitted = models.DateField()
	candidate_name = models.CharField()
	current_status = models.IntegerField()
	current_status_desc = models.CharField()
	interview_date = models.DateField()
	remarks = models.CharField()
	skills = models.CharField()
	current_org = models.CharField()
	qualification = models.CharField()
	total_exp = models.FloatField()
	current_location = models.CharField()
	contact_details_mobile = models.IntegerField(max_len = 10, unique_key = True)
	contact_details_mobile = models.IntegerField(max_len = 10, unique_key = True)
	email = models.CharField()
    expected_salary_percentage = models.IntegerField()
    expected_salary_amt = models.FloatField()
    notice_period = models.IntegerField()
    Int_Tele_date = models.DateField()
    Int_Tele_result = models.CharField()
    Int_P1_date = models.DateField()
    Int_P1_result = models.CharField()
    Int_p2_date = models.DateField()
    Int_p2_result = models.Charfield()
    Int_p3_date = models.DateField()
    Int_p3_result = models.Charfield()
    Int_Final_date = models.DateField()
    Int_Final_result = models.Charfield()
    Int_HR_date = models.DateField()
    Int_HR_result = models.Charfield()
    offer_date = models.DateField()
    offer_amt = models.FloatField()
    joining_date = models.DateField()
    vacancy_code = models.Charfield()
    applicant_code = models.Charfield()
    DOB = models.DateField()
    preffered_company = models.Charfield()
    preffered_location = models.Charfield()
    week_number = models.IntegerField()
    wk_year = models.IntegerField()


class bad_records(models.Model):
	sr_no = models.IntegerField(auto_now_add = True, unique_key = True)
	recruiter = models.CharField(foriegn_key = True)
	client = models.CharField(foriegn_key = True)
	position = models.AlphaNumericField()
	reqt_date = models.DateField()
	date_cv_submitted = models.DateField()
	candidate_name = models.CharField()
	current_status = models.IntegerField()
	current_status_desc = models.CharField()
	interview_date = models.DateField()
	remarks = models.CharField()
	skills = models.CharField()
	current_org = models.CharField()
	qualification = models.CharField()
	total_exp = models.FloatField()
	current_location = models.CharField()
	contact_details_mobile = models.IntegerField(max_len = 10, unique_key = True)
	contact_details_mobile = models.IntegerField(max_len = 10, unique_key = True)
	email = models.CharField()
    expected_salary_percentage = models.IntegerField()
    expected_salary_amt = models.FloatField()
    notice_period = models.IntegerField()
    Int_Tele_date = models.DateField()
    Int_Tele_result = models.CharField()
    Int_P1_date = models.DateField()
    Int_P1_result = models.CharField()
    Int_p2_date = models.DateField()
    Int_p2_result = models.Charfield()
    Int_p3_date = models.DateField()
    Int_p3_result = models.Charfield()
    Int_Final_date = models.DateField()
    Int_Final_result = models.Charfield()
    Int_HR_date = models.DateField()
    Int_HR_result = models.Charfield()
    offer_date = models.DateField()
    offer_amt = models.FloatField()
    joining_date = models.DateField()
    vacancy_code = models.Charfield()
    applicant_code = models.Charfield()
    DOB = models.DateField()
    preffered_company = models.Charfield()
    preffered_location = models.Charfield()
    week_number = models.IntegerField()
    wk_year = models.IntegerField()
    reason = models.Charfield()