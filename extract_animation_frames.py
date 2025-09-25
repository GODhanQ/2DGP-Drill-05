import numpy as np
from PIL import Image
import json

def extract_frame_data(image_path, rows=4, frames_per_row=8):
    """
    애니메이션 시트에서 각 프레임의 left, bottom, width, height 데이터를 추출합니다.

    Args:
        image_path: 애니메이션 시트 이미지 경로
        rows: 행의 개수 (기본값: 4)
        frames_per_row: 각 행의 프레임 개수 (기본값: 8)

    Returns:
        각 프레임의 좌표 데이터가 담긴 딕셔너리 리스트
    """

    # 이미지 로드
    try:
        image = Image.open(image_path)
        print(f"이미지 로드 성공: {image_path}")
        print(f"이미지 크기: {image.size[0]} x {image.size[1]}")
    except Exception as e:
        print(f"이미지 로드 실패: {e}")
        return None

    # 이미지 크기
    img_width, img_height = image.size

    # 각 프레임의 크기 계산
    frame_width = img_width // frames_per_row
    frame_height = img_height // rows

    print(f"각 프레임 크기: {frame_width} x {frame_height}")
    print(f"총 프레임 개수: {rows * frames_per_row}")

    # 프레임 데이터 추출
    frame_data = []

    for row in range(rows):
        for col in range(frames_per_row):
            # left: x 좌표 (왼쪽부터의 거리)
            left = col * frame_width

            # bottom: y 좌표 (아래쪽부터의 거리)
            # 이미지에서는 위쪽이 0이므로, 아래쪽부터 계산하려면 변환 필요
            top = row * frame_height
            bottom = img_height - top - frame_height

            # width, height: 프레임의 크기
            width = frame_width
            height = frame_height

            frame_info = {
                'row': row,
                'col': col,
                'frame_index': row * frames_per_row + col,
                'left': left,
                'bottom': bottom,
                'width': width,
                'height': height,
                'top': top,  # 참고용으로 추가
                'right': left + width  # 참고용으로 추가
            }

            frame_data.append(frame_info)

            print(f"프레임 [{row}][{col}]: left={left}, bottom={bottom}, width={width}, height={height}")

    return frame_data

def save_frame_data(frame_data, output_file):
    """프레임 데이터를 JSON 파일로 저장"""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(frame_data, f, indent=2, ensure_ascii=False)
        print(f"프레임 데이터가 {output_file}에 저장되었습니다.")
    except Exception as e:
        print(f"파일 저장 실패: {e}")

def extract_individual_frames(image_path, frame_data, output_dir="frames"):
    """각 프레임을 개별 이미지 파일로 저장 (선택사항)"""
    import os

    try:
        image = Image.open(image_path)

        # 출력 디렉토리 생성
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for frame in frame_data:
            # 프레임 영역 크롭 (left, top, right, bottom)
            crop_box = (
                frame['left'],
                frame['top'],
                frame['right'],
                frame['top'] + frame['height']
            )

            cropped_frame = image.crop(crop_box)

            # 파일명 생성
            filename = f"frame_r{frame['row']}_c{frame['col']}.png"
            filepath = os.path.join(output_dir, filename)

            cropped_frame.save(filepath)

        print(f"모든 프레임이 {output_dir} 디렉토리에 저장되었습니다.")

    except Exception as e:
        print(f"개별 프레임 저장 실패: {e}")

def main():
    # 애니메이션 시트 경로
    animation_sheet_path = "Lecture06_HandlingInputs/animation_sheet.png"

    # 행과 열 설정 (필요에 따라 조정)
    rows = 4  # 4개 행
    frames_per_row = 8  # 각 행마다 8개 프레임 (예시)

    print("=== 애니메이션 시트 프레임 추출기 ===")
    print(f"대상 파일: {animation_sheet_path}")

    # 프레임 데이터 추출
    frame_data = extract_frame_data(animation_sheet_path, rows, frames_per_row)

    if frame_data:
        # JSON 파일로 저장
        save_frame_data(frame_data, "frame_coordinates.json")

        # 개별 프레임 이미지로 저장 (선택사항)
        extract_individual_frames(animation_sheet_path, frame_data)

        print("\n=== 추출 완료 ===")
        print(f"총 {len(frame_data)}개의 프레임 데이터가 추출되었습니다.")

        # 첫 번째와 마지막 프레임 정보 출력
        print(f"\n첫 번째 프레임: {frame_data[0]}")
        print(f"마지막 프레임: {frame_data[-1]}")
    else:
        print("프레임 데이터 추출에 실패했습니다.")

if __name__ == "__main__":
    main()
