import cv2 as cv
from dt_apriltags import Detector

class AprilTagProcessor:
    def __init__(self):
        # Initialiseer de detector voor de 36h11 familie (meest gebruikt)
        self.detector = Detector(families='tag36h11',
                                 nthreads=1,
                                 quad_decimate=1.0,
                                 quad_sigma=0.0,
                                 refine_edges=1,
                                 decode_sharpening=0.25,
                                 debug=0)

    def get_error(self, frame):
        # 1. AprilTags hebben grijswaarden nodig
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
        # 2. Detecteer tags
        # We hoeven hier geen model te laden, de wiskunde zit in de library
        tags = self.detector.detect(gray)

        h, w = gray.shape
        midden_x = w // 2
        midden_y = h // 2
        error_x = 0
        error_y = 0

        # Rode middenlijnen tekenen
        cv.line(frame, (midden_x, 0), (midden_x, h), (0, 0, 255), 1)
        cv.line(frame, (0, midden_y), (w, midden_y), (0, 0, 255), 1)

        if len(tags) > 0:
            # We pakken de eerste tag die we vinden
            tag = tags[0]
            
            # Het centrum van de tag (x, y)
            tag_center_x = int(tag.center[0])
            tag_center_y = int(tag.center[1])

            # Bereken de afwijking (error)
            error_x = tag_center_x - midden_x
            error_y = tag_center_y - midden_y

            # Teken de omtrek van de tag
            for i in range(4):
                start_point = tuple(tag.corners[i].astype(int))
                end_point = tuple(tag.corners[(i + 1) % 4].astype(int))
                cv.line(frame, start_point, end_point, (0, 255, 0), 2)

            # Teken een kruis op het midden van de tag
            cv.drawMarker(frame, (tag_center_x, tag_center_y), (0, 255, 0), cv.MARKER_CROSS, 15, 2)
            
            # Toon info
            cv.putText(frame, f"ID: {tag.tag_id} | ErrX: {error_x} ErrY: {error_y}", 
                       (10, 50), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        return frame, error_x, error_y