import os
import django
from datetime import datetime, timedelta

# Django 설정 로드
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from categories.models import Category
from houses.models import House
from rooms.models import Room, Amenity
from reviews.models import Review
from experiences.models import Experience, Perk

User = get_user_model()

# 사용자 데이터 생성
def create_users():
    users = [
        {
            "username": "admin",
            "email": "admin@example.com",
            "password": "admin123",
            "name": "관리자",
            "is_host": True,
            "gender": "M",
            "language": "KR",
            "currency": "KRW",
        },
        {
            "username": "user1",
            "email": "user1@example.com",
            "password": "user123",
            "name": "홍길동",
            "is_host": False,
            "gender": "M",
            "language": "KR",
            "currency": "KRW",
        },
        {
            "username": "user2",
            "email": "user2@example.com",
            "password": "user123",
            "name": "김철수",
            "is_host": True,
            "gender": "M",
            "language": "KR",
            "currency": "KRW",
        },
        {
            "username": "user3",
            "email": "user3@example.com",
            "password": "user123",
            "name": "이영희",
            "is_host": False,
            "gender": "F",
            "language": "EN",
            "currency": "USD",
        },
    ]
    
    created_users = []
    for user_data in users:
        user, created = User.objects.get_or_create(
            username=user_data["username"],
            defaults={
                "email": user_data["email"],
                "name": user_data["name"],
                "is_host": user_data["is_host"],
                "gender": user_data["gender"],
                "language": user_data["language"],
                "currency": user_data["currency"],
            }
        )
        if created:
            user.set_password(user_data["password"])
            user.save()
            print(f"사용자 생성: {user.username}")
        else:
            print(f"사용자 이미 존재: {user.username}")
        created_users.append(user)
    
    return created_users

# 카테고리 데이터 생성
def create_categories():
    categories = [
        {"name": "해변 근처", "kind": "rooms"},
        {"name": "모던함", "kind": "rooms"},
        {"name": "전통적인", "kind": "rooms"},
        {"name": "요리", "kind": "experiences"},
        {"name": "모험", "kind": "experiences"},
    ]
    
    created_categories = []
    for category_data in categories:
        category, created = Category.objects.get_or_create(
            name=category_data["name"],
            defaults={"kind": category_data["kind"]}
        )
        if created:
            print(f"카테고리 생성: {category.name}")
        else:
            print(f"카테고리 이미 존재: {category.name}")
        created_categories.append(category)
    
    return created_categories

# 집 데이터 생성
def create_houses(users):
    houses = [
        {
            "name": "서울 타워 하우스",
            "address": "서울시 용산구 남산동",
            "price": 500000000,
            "year": 2015,
            "area": 120,
            "bedrooms": 3,
            "bathrooms": 2.0,
            "floors": 2,
            "parking": True,
            "garden": True,
            "pool": False,
            "pets_allowed": True,
            "owner": users[0],  # admin
        },
        {
            "name": "부산 해변 빌라",
            "address": "부산시 해운대구 우동",
            "price": 700000000,
            "year": 2018,
            "area": 150,
            "bedrooms": 4,
            "bathrooms": 3.0,
            "floors": 3,
            "parking": True,
            "garden": True,
            "pool": True,
            "pets_allowed": False,
            "owner": users[2],  # user2
        },
        {
            "name": "제주 전통 한옥",
            "address": "제주시 애월읍",
            "price": 400000000,
            "year": 2010,
            "area": 100,
            "bedrooms": 2,
            "bathrooms": 1.5,
            "floors": 1,
            "parking": True,
            "garden": True,
            "pool": False,
            "pets_allowed": True,
            "owner": users[0],  # admin
        },
        {
            "name": "강원도 산장",
            "address": "강원도 평창군",
            "price": 350000000,
            "year": 2012,
            "area": 90,
            "bedrooms": 2,
            "bathrooms": 1.0,
            "floors": 1,
            "parking": True,
            "garden": True,
            "pool": False,
            "pets_allowed": True,
            "owner": users[2],  # user2
        },
    ]
    
    created_houses = []
    for house_data in houses:
        house, created = House.objects.get_or_create(
            name=house_data["name"],
            defaults={
                "address": house_data["address"],
                "price": house_data["price"],
                "year": house_data["year"],
                "area": house_data["area"],
                "bedrooms": house_data["bedrooms"],
                "bathrooms": house_data["bathrooms"],
                "floors": house_data["floors"],
                "parking": house_data["parking"],
                "garden": house_data["garden"],
                "pool": house_data["pool"],
                "pets_allowed": house_data["pets_allowed"],
                "owner": house_data["owner"],
            }
        )
        if created:
            print(f"집 생성: {house.name}")
        else:
            print(f"집 이미 존재: {house.name}")
        created_houses.append(house)
    
    return created_houses

# 편의시설 데이터 생성
def create_amenities():
    amenities = [
        {"name": "와이파이", "description": "고속 인터넷 연결"},
        {"name": "에어컨", "description": "시원한 냉방 시설"},
        {"name": "주방", "description": "요리를 할 수 있는 공간"},
        {"name": "세탁기", "description": "의류 세탁 가능"},
        {"name": "TV", "description": "엔터테인먼트 시설"},
        {"name": "수영장", "description": "실내 또는 실외 수영장"},
        {"name": "주차장", "description": "무료 주차 공간"},
    ]
    
    created_amenities = []
    for amenity_data in amenities:
        amenity, created = Amenity.objects.get_or_create(
            name=amenity_data["name"],
            defaults={"description": amenity_data["description"]}
        )
        if created:
            print(f"편의시설 생성: {amenity.name}")
        else:
            print(f"편의시설 이미 존재: {amenity.name}")
        created_amenities.append(amenity)
    
    return created_amenities

# 방 데이터 생성
def create_rooms(users, houses, categories, amenities):
    rooms = [
        {
            "name": "서울 타워 하우스 - 마스터룸",
            "country": "대한민국",
            "city": "서울",
            "price": 100000,
            "address": "서울시 용산구 남산동 123",
            "bathrooms": 1.5,
            "bedrooms": 1,
            "room_type": "Private",
            "description": "서울 타워가 보이는 아름다운 전망의 마스터룸입니다.",
            "owner": users[0],  # admin
            "house": houses[0],  # 서울 타워 하우스
            "category": categories[1],  # 모던함
        },
        {
            "name": "부산 해변 빌라 - 오션뷰룸",
            "country": "대한민국",
            "city": "부산",
            "price": 150000,
            "address": "부산시 해운대구 우동 456",
            "bathrooms": 1.0,
            "bedrooms": 1,
            "room_type": "Entire",
            "description": "해운대 해변이 보이는 전체 독채 숙소입니다.",
            "owner": users[2],  # user2
            "house": houses[1],  # 부산 해변 빌라
            "category": categories[0],  # 해변 근처
        },
        {
            "name": "제주 전통 한옥 - 온돌방",
            "country": "대한민국",
            "city": "제주",
            "price": 80000,
            "address": "제주시 애월읍 789",
            "bathrooms": 1.0,
            "bedrooms": 1,
            "room_type": "Private",
            "description": "제주의 전통 한옥에서 온돌방을 체험해보세요.",
            "owner": users[0],  # admin
            "house": houses[2],  # 제주 전통 한옥
            "category": categories[2],  # 전통적인
        },
        {
            "name": "강원도 산장 - 통나무집",
            "country": "대한민국",
            "city": "평창",
            "price": 120000,
            "address": "강원도 평창군 101112",
            "bathrooms": 1.0,
            "bedrooms": 2,
            "room_type": "Entire",
            "description": "강원도 산속에 위치한 아늑한 통나무집입니다.",
            "owner": users[2],  # user2
            "house": houses[3],  # 강원도 산장
            "category": categories[2],  # 전통적인
        },
    ]
    
    created_rooms = []
    for room_data in rooms:
        room, created = Room.objects.get_or_create(
            name=room_data["name"],
            defaults={
                "country": room_data["country"],
                "city": room_data["city"],
                "price": room_data["price"],
                "address": room_data["address"],
                "bathrooms": room_data["bathrooms"],
                "bedrooms": room_data["bedrooms"],
                "room_type": room_data["room_type"],
                "description": room_data["description"],
                "owner": room_data["owner"],
                "house": room_data["house"],
                "category": room_data["category"],
            }
        )
        if created:
            # 편의시설 추가 (랜덤하게 3-4개)
            import random
            selected_amenities = random.sample(amenities, random.randint(3, min(4, len(amenities))))
            room.amenities.set(selected_amenities)
            print(f"방 생성: {room.name}")
        else:
            print(f"방 이미 존재: {room.name}")
        created_rooms.append(room)
    
    return created_rooms

# Perk 데이터 생성
def create_perks():
    perks = [
        {"name": "음료 제공", "details": "무료 음료가 제공됩니다."},
        {"name": "장비 대여", "details": "필요한 모든 장비를 대여해 드립니다."},
        {"name": "교통편 제공", "details": "픽업 및 드롭오프 서비스가 포함되어 있습니다."},
        {"name": "전문 가이드", "details": "경험이 풍부한 전문 가이드가 안내합니다."},
        {"name": "사진 촬영", "details": "전문 사진작가가 체험을 촬영해 드립니다."},
        {"name": "간식 제공", "details": "현지 간식이 제공됩니다."},
    ]
    
    created_perks = []
    for perk_data in perks:
        perk, created = Perk.objects.get_or_create(
            name=perk_data["name"],
            defaults={"details": perk_data["details"]}
        )
        if created:
            print(f"특전 생성: {perk.name}")
        else:
            print(f"특전 이미 존재: {perk.name}")
        created_perks.append(perk)
    
    return created_perks

# 체험 데이터 생성
def create_experiences(users, categories, perks):
    # 시작 시간 설정 (현재로부터 1주일 후)
    start_date = datetime.now() + timedelta(days=7)
    
    experiences = [
        {
            "name": "서울 한강 자전거 투어",
            "host": users[0],  # admin
            "country": "대한민국",
            "city": "서울",
            "price": 50000,
            "duration": 3,  # 시간
            "address": "서울시 영등포구 여의도공원",
            "starts_at": start_date.replace(hour=10, minute=0),
            "ends_at": start_date.replace(hour=13, minute=0),
            "description": "한강을 따라 자전거를 타며 서울의 아름다운 경치를 감상하는 투어입니다.",
            "category": categories[4],  # 모험
        },
        {
            "name": "부산 해산물 요리 클래스",
            "host": users[2],  # user2
            "country": "대한민국",
            "city": "부산",
            "price": 70000,
            "duration": 2,  # 시간
            "address": "부산시 해운대구 중동",
            "starts_at": start_date.replace(hour=18, minute=0),
            "ends_at": start_date.replace(hour=20, minute=0),
            "description": "신선한 해산물로 맛있는 한국 요리를 배우는 쿠킹 클래스입니다.",
            "category": categories[3],  # 요리
        },
        {
            "name": "제주 올레길 트레킹",
            "host": users[0],  # admin
            "country": "대한민국",
            "city": "제주",
            "price": 40000,
            "duration": 4,  # 시간
            "address": "제주시 구좌읍",
            "starts_at": start_date.replace(hour=9, minute=0),
            "ends_at": start_date.replace(hour=13, minute=0),
            "description": "제주 올레길을 따라 아름다운 자연 경관을 감상하며 걷는 트레킹 체험입니다.",
            "category": categories[4],  # 모험
        },
        {
            "name": "강원도 전통주 만들기",
            "host": users[2],  # user2
            "country": "대한민국",
            "city": "강원",
            "price": 60000,
            "duration": 3,  # 시간
            "address": "강원도 평창군",
            "starts_at": start_date.replace(hour=14, minute=0),
            "ends_at": start_date.replace(hour=17, minute=0),
            "description": "강원도 전통 방식으로 막걸리를 직접 만들어보는 체험입니다.",
            "category": categories[3],  # 요리
        },
    ]
    
    created_experiences = []
    for exp_data in experiences:
        experience, created = Experience.objects.get_or_create(
            name=exp_data["name"],
            defaults={
                "host": exp_data["host"],
                "country": exp_data["country"],
                "city": exp_data["city"],
                "price": exp_data["price"],
                "duration": exp_data["duration"],
                "address": exp_data["address"],
                "starts_at": exp_data["starts_at"],
                "ends_at": exp_data["ends_at"],
                "description": exp_data["description"],
                "category": exp_data["category"],
            }
        )
        if created:
            # 특전 추가 (랜덤하게 2-3개)
            import random
            selected_perks = random.sample(perks, random.randint(2, min(3, len(perks))))
            experience.perks.set(selected_perks)
            print(f"체험 생성: {experience.name}")
        else:
            print(f"체험 이미 존재: {experience.name}")
        created_experiences.append(experience)
    
    return created_experiences

# 리뷰 데이터 생성 함수 수정
def create_reviews(users, rooms, experiences):
    # 방에 대한 리뷰
    room_reviews = [
        # 서울 타워 하우스 - 마스터룸 리뷰
        {
            "user": users[1],  # user1
            "review": "정말 좋은 숙소였습니다. 깨끗하고 전망도 좋았어요.",
            "room": rooms[0],
            "experience": None,
            "rating": 5,
        },
        {
            "user": users[3],  # user3
            "review": "위치가 좋고 호스트가 친절했습니다.",
            "room": rooms[0],
            "experience": None,
            "rating": 4,
        },
        {
            "user": users[2],  # user2
            "review": "시설이 좋고 편안했습니다. 다음에 또 이용하고 싶어요.",
            "room": rooms[0],
            "experience": None,
            "rating": 5,
        },
        
        # 부산 해변 빌라 - 오션뷰룸 리뷰
        {
            "user": users[1],  # user1
            "review": "해변이 가까워서 좋았지만 조금 시끄러웠어요.",
            "room": rooms[1],
            "experience": None,
            "rating": 3,
        },
        {
            "user": users[3],  # user3
            "review": "뷰가 정말 환상적이었습니다. 해변이 바로 보여요!",
            "room": rooms[1],
            "experience": None,
            "rating": 5,
        },
        {
            "user": users[0],  # admin
            "review": "시설은 좋았지만 주변이 조금 시끄러웠습니다.",
            "room": rooms[1],
            "experience": None,
            "rating": 4,
        },
        
        # 제주 전통 한옥 - 온돌방 리뷰
        {
            "user": users[3],  # user3
            "review": "전통적인 한옥 체험이 정말 좋았습니다.",
            "room": rooms[2],
            "experience": None,
            "rating": 5,
        },
        {
            "user": users[1],  # user1
            "review": "독특한 경험이었고 호스트가 매우 친절했어요.",
            "room": rooms[2],
            "experience": None,
            "rating": 4,
        },
        {
            "user": users[2],  # user2
            "review": "제주도의 전통을 느낄 수 있는 좋은 숙소였습니다.",
            "room": rooms[2],
            "experience": None,
            "rating": 5,
        },
        
        # 강원도 산장 - 통나무집 리뷰
        {
            "user": users[0],  # admin
            "review": "조용하고 평화로운 곳이었습니다. 자연을 느끼기 좋아요.",
            "room": rooms[3],
            "experience": None,
            "rating": 5,
        },
        {
            "user": users[1],  # user1
            "review": "겨울에 방문했는데 따뜻하고 아늑했어요.",
            "room": rooms[3],
            "experience": None,
            "rating": 4,
        },
        {
            "user": users[3],  # user3
            "review": "산속에 있어 공기가 맑고 경치가 좋았습니다.",
            "room": rooms[3],
            "experience": None,
            "rating": 5,
        },
    ]
    
    # 체험에 대한 리뷰
    experience_reviews = [
        # 서울 한강 자전거 투어 리뷰
        {
            "user": users[1],  # user1
            "review": "한강의 아름다운 경치를 자전거로 즐길 수 있어 좋았습니다.",
            "room": None,
            "experience": experiences[0],
            "rating": 5,
        },
        {
            "user": users[3],  # user3
            "review": "가이드가 친절하고 코스도 좋았어요.",
            "room": None,
            "experience": experiences[0],
            "rating": 4,
        },
        {
            "user": users[2],  # user2
            "review": "자전거 상태가 좋았고 안전하게 즐길 수 있었습니다.",
            "room": None,
            "experience": experiences[0],
            "rating": 5,
        },
        
        # 부산 해산물 요리 클래스 리뷰
        {
            "user": users[0],  # admin
            "review": "신선한 해산물로 맛있는 요리를 배울 수 있어 좋았습니다.",
            "room": None,
            "experience": experiences[1],
            "rating": 5,
        },
        {
            "user": users[1],  # user1
            "review": "강사님이 친절하게 가르쳐주셔서 쉽게 따라할 수 있었어요.",
            "room": None,
            "experience": experiences[1],
            "rating": 4,
        },
        {
            "user": users[3],  # user3
            "review": "부산의 신선한 해산물로 요리하는 법을 배워 유익했습니다.",
            "room": None,
            "experience": experiences[1],
            "rating": 5,
        },
        
        # 제주 올레길 트레킹 리뷰
        {
            "user": users[1],  # user1
            "review": "제주의 아름다운 자연을 느낄 수 있는 좋은 경험이었습니다.",
            "room": None,
            "experience": experiences[2],
            "rating": 5,
        },
        {
            "user": users[2],  # user2
            "review": "가이드의 설명이 자세하고 코스도 적당했습니다.",
            "room": None,
            "experience": experiences[2],
            "rating": 4,
        },
        {
            "user": users[3],  # user3
            "review": "올레길의 아름다움을 제대로 느낄 수 있었어요.",
            "room": None,
            "experience": experiences[2],
            "rating": 5,
        },
        
        # 강원도 전통주 만들기 리뷰
        {
            "user": users[0],  # admin
            "review": "전통주 만드는 과정을 배울 수 있어 유익했습니다.",
            "room": None,
            "experience": experiences[3],
            "rating": 4,
        },
        {
            "user": users[1],  # user1
            "review": "직접 만든 술을 가져갈 수 있어 좋았어요.",
            "room": None,
            "experience": experiences[3],
            "rating": 5,
        },
        {
            "user": users[3],  # user3
            "review": "강원도의 전통을 배울 수 있는 좋은 기회였습니다.",
            "room": None,
            "experience": experiences[3],
            "rating": 4,
        },
    ]
    
    # 모든 리뷰 합치기
    all_reviews = room_reviews + experience_reviews
    
    created_reviews = []
    for review_data in all_reviews:
        # 방 리뷰인 경우
        if review_data["room"]:
            review, created = Review.objects.get_or_create(
                user=review_data["user"],
                room=review_data["room"],
                defaults={
                    "review": review_data["review"],
                    "experience": None,
                    "rating": review_data["rating"],
                }
            )
            if created:
                print(f"리뷰 생성: {review.user.username}의 {review.room.name} 리뷰")
            else:
                print(f"리뷰 이미 존재: {review.user.username}의 {review.room.name} 리뷰")
        
        # 체험 리뷰인 경우
        elif review_data["experience"]:
            review, created = Review.objects.get_or_create(
                user=review_data["user"],
                experience=review_data["experience"],
                defaults={
                    "review": review_data["review"],
                    "room": None,
                    "rating": review_data["rating"],
                }
            )
            if created:
                print(f"리뷰 생성: {review.user.username}의 {review.experience.name} 리뷰")
            else:
                print(f"리뷰 이미 존재: {review.user.username}의 {review.experience.name} 리뷰")
        
        created_reviews.append(review)
    
    return created_reviews

# 모든 데이터 생성 실행
def create_all_mock_data():
    print("목 데이터 생성을 시작합니다...")
    users = create_users()
    categories = create_categories()
    amenities = create_amenities()
    perks = create_perks()
    houses = create_houses(users)
    rooms = create_rooms(users, houses, categories, amenities)
    experiences = create_experiences(users, categories, perks)
    reviews = create_reviews(users, rooms, experiences)
    print("목 데이터 생성이 완료되었습니다!")

if __name__ == "__main__":
    create_all_mock_data() 