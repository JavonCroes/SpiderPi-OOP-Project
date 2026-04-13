import cv2 as cv
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class FaceProcessor:
    def __init__(self):
        self.model = "face_landmarker_v2_with_blendshapes.task"
        
        self.base_options = python.BaseOptions(model_asset_path=self.model)
        self.options = vision.FaceLandmarkerOptions(
            base_options=self.base_options,
            running_mode=vision.RunningMode.IMAGE,
            num_faces=1
        )
        self.landmarker = vision.FaceLandmarker.create_from_options(self.options)

    def get_error(self, frame):
            rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            result = self.landmarker.detect(mp_image)
    
            h, w, _ = frame.shape
            midden_beeld = w // 2
            error_x = 0
    
            cv.line(frame, (midden_beeld, 0), (midden_beeld, h), (0, 0, 255), 1)
    
            if result.face_landmarks:
                alle_punten = result.face_landmarks[0]
    
                som_x = 0
                som_y = 0
                for landmark in alle_punten:
                    px = int(landmark.x * w)
                    py = int(landmark.y * h)
                    cv.circle(frame, (px, py), 1, (255, 0, 0), -1)
                    som_x += px
                    som_y += py
    
                # Gemiddelde berekenen
                gezicht_center_x = som_x // len(alle_punten)
                gezicht_center_y = som_y // len(alle_punten)
    
                error_x = gezicht_center_x - midden_beeld
    
                cv.drawMarker(frame, (gezicht_center_x, gezicht_center_y), (0, 255, 0), cv.MARKER_CROSS, 20, 2)
                
                # Tekst met  error
                cv.putText(frame, f"Error: {error_x} px", (10, 50), 
                           cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            return frame, error_x