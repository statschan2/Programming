-- 코드를 입력하세요
SELECT b.ingredient_type, sum(total_order) as TOTAL_ORDER
from first_half a
    join icecream_info b on a.flavor = b.flavor
group by b.ingredient_type
order by 2