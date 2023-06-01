-- 코드를 입력하세요
SELECT a.product_code as PRODUCT_CODE, sum(a.price * b.sales_amount) as SALES
from product a
    join offline_sale b on a.product_id = b.product_id
group by a.product_code
order by 2 desc, 1
