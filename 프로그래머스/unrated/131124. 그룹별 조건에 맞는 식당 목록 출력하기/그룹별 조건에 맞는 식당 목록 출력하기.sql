select mp.member_name, rr.review_text, left(rr.review_date,10)
from member_profile as mp
join rest_review as rr
on mp.member_id = rr.member_id
where mp.member_id = (select member_id 
                      from rest_review
                      group by member_id
                      order by count(member_id) desc
                      limit 1
                     )
order by rr.review_date
                     

# select mp.member_name, rr.review_text, left(rr.review_date,10)
# from member_profile as mp
# join rest_review as rr
# on mp.member_id = rr.member_id
# where mp.member_id = (
#     select member_id
#     from rest_review
#     group by rest_review.member_id
#     order by count(member_id) desc
#     limit 1
# )
# order by rr.review_date