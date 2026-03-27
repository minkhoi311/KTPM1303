python -m pytest tests/ -v --cov=src --cov-report=term-missing

Dùng để đổ độ che phu

Coverage và xuất file html
python -m pytest tests/ --cov=src --cov-report=html 
kiểm tra dưới bao nhiêu % nè
python -m pytest tests/ --cov=src --cov-fail-under=100 
