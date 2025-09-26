import calendar
import datetime
from flask import current_app, request

from app.models.plan import Plans, db

def create_plan():
    data = request.get_json()  # 从请求体里解析 JSON
    userid = data.get("userid")
    plan_date = data.get("selectedDate")
    title = data.get("title")
    start = data.get("start")
    end = data.get("end")

    if not userid or not userid:
        return {'code': 400, 'msg': '请重新登录'}
    if not plan_date or not plan_date:
        return {'code': 400, 'msg': '日期不能为空'}
    if not title or not title:
        return {'code': 400, 'msg': '内容不能为空'}
    if not start or not start:
        return {'code': 400, 'msg': '开始时间不能为空'}
    if not end or not end:
        return {'code': 400, 'msg': '结束时间不能为空'}
    
    plan = Plans(userid=userid, plan_date=plan_date, title=title, start_time=start, end_time=end)

    with current_app.app_context():
        db.session.add(plan)
        db.session.commit()

    return {'code': 200, 'msg': 'success'}

def get_month_plans():
    # 获取 userid
    auth_header = request.headers.get("Authorization")
    userid = None
    if auth_header and auth_header.startswith("Bearer "):
        userid = auth_header.split(" ")[1]
    year = request.args.get("year",type=int)
    month = request.args.get("month", type=int)
    
     # 第一天
    first_day = datetime.date(year, month, 1)
    # 获取当月天数
    last_day_num = calendar.monthrange(year, month)[1]
    # 最后一天
    last_day = datetime.date(year, month, last_day_num)

    with current_app.app_context():
        plans = Plans.query.filter(Plans.userid == userid).filter(Plans.plan_date.between(first_day, last_day)).all()

    return {'code': 200, 'msg': 'success', 'data': [p.to_dict() for p in plans]}

def get_day_plans():
    # 获取 userid
    auth_header = request.headers.get("Authorization")
    userid = None
    if auth_header and auth_header.startswith("Bearer "):
        userid = auth_header.split(" ")[1]

    day = request.args.get("day")

    with current_app.app_context():
        plans = Plans.query.filter(Plans.userid == userid).filter(Plans.plan_date == day).all()
    return {'code': 200, 'msg': 'success', 'data': [p.to_dict() for p in plans]}