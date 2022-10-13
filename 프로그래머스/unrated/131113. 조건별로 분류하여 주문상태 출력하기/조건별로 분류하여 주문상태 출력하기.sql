select order_id, product_id, left(out_date, 10),
case 
    when out_date is null then "출고미정"
    when datediff(out_date, '2022-05-01')<=0 then "출고완료"
    when datediff(out_date, '2022-05-01')>0 Then "출고대기"
end
from food_order










# select order_id, product_id, substr(out_date,1,10),
# case
#     when out_date is null then "출고미정"
#     when datediff(out_date, '2022-05-01') > 0 then "출고대기"
#     when datediff(out_date, '2022-05-01') <= 0 then "출고완료"
# end

# from food_order
# order by order_id