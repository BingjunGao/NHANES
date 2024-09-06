# ʹ��Python�ٷ�����������
FROM python:3.12.3-slim

# ���ù���Ŀ¼
WORKDIR /app

# ������Ŀ�ļ�
COPY . .

# ��װ����
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ��¶FlaskĬ�ϵ����ж˿�
EXPOSE 5000

# ����FlaskӦ��
CMD ["flask", "run", "--host=0.0.0.0"]
