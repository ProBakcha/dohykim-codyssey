#!/bin/bash

echo "🔍 1. DockerHub에서 ubuntu 이미지 검색 중..."
docker search ubuntu

echo "📥 2. ubuntu:20.04 이미지 다운로드 중..."
docker pull ubuntu:20.04

echo "ℹ️ 3. 이미지 상세 정보:"
docker inspect ubuntu:20.04 | head -n 20

echo "📜 4. 이미지 히스토리:"
docker history ubuntu:20.04

echo "🚀 5. 컨테이너 실행 및 /tmp/hello.txt 파일 생성..."
CID=$(docker run -dit ubuntu:20.04 bash)
docker exec $CID bash -c "touch /tmp/hello.txt && echo 'File created in container.'"

echo "📄 6. 컨테이너 내부 파일 목록 (/tmp):"
docker exec $CID ls /tmp

echo "🛑 7. 컨테이너 종료 및 삭제..."
docker stop $CID > /dev/null
docker rm $CID > /dev/null

echo "🔄 8. 동일 이미지로 컨테이너 재실행..."
CID2=$(docker run -dit ubuntu:20.04 bash)

echo "📁 9. 새로운 컨테이너에서 파일 존재 여부 확인 (/tmp):"
docker exec $CID2 ls /tmp | grep hello.txt && echo "❗️파일이 남아 있음 (예외적 상황)" || echo "✅ 파일이 존재하지 않음 (정상)"

echo "🧹 10. 컨테이너 정리..."
docker stop $CID2 > /dev/null
docker rm $CID2 > /dev/null

echo "✅ 모든 실습 완료!"
