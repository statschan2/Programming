-- 코드를 입력하세요
select dr_name, dr_id, mcdp_cd, DATE_FORMAT(hire_ymd,'%Y-%m-%d') as HIRE_YMD
from doctor
where mcdp_cd in ("CS","GS")
order by HIRE_YMD desc, dr_name

# SELECT dr_name, dr_id, mcdp_cd, DATE_FORMAT(hire_ymd, '%Y-%m-%d') as hire_ymd
# from doctor
# where mcdp_cd in ('cs', 'gs')
# order by hire_ymd desc, dr_name