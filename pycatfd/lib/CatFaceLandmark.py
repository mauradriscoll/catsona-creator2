class CatFaceLandmark:
    CHIN = 0
    # CHIN_LEFT = 1
    # CHIN_RIGHT = 2
    LEFT_EYE = 1
    # LEFT_EYE_LEFT = 4
    # LEFT_EYE_RIGHT = 5 
    # LEFT_EYE_ABOVE = 6
    # LEFT_EYE_BELOW = 7
    LEFT_OF_LEFT_EAR = 2
    LEFT_OF_RIGHT_EAR = 3
    NOSE = 4
    # NOSE_LEFT = 11
    # NOSE_RIGHT = 12
    # NOSE_BELOW = 13
    RIGHT_EYE = 5
    # RIGHT_EYE_LEFT = 15
    # RIGHT_EYE_RIGHT = 16
    # RIGHT_EYE_ABOVE = 17
    # RIGHT_EYE_BELOW = 18
    RIGHT_OF_LEFT_EAR = 6
    RIGHT_OF_RIGHT_EAR = 7




    def __init__(self):
        pass

    @staticmethod
    def all():
        return [
            {
                'value': CatFaceLandmark.CHIN,
                'name': 'Chin'
            },
            # {
            #     'value': CatFaceLandmark.CHIN_LEFT,
            #     'name': 'Chin Left'
            # },
            # {
            #     'value': CatFaceLandmark.CHIN_RIGHT,
            #     'name': 'Chin Right'
            # },
            {
                'value': CatFaceLandmark.LEFT_EYE,
                'name': 'Left Eye'
            },
            # {
            #     'value': CatFaceLandmark.LEFT_EYE_LEFT,
            #     'name': 'Left Eye Left'
            # },
            # {
            #     'value': CatFaceLandmark.LEFT_EYE_RIGHT,
            #     'name': 'Left Eye Right'
            # },
            # {
            #     'value': CatFaceLandmark.LEFT_EYE_ABOVE,
            #     'name': 'Left Eye Above'
            # },
            # {
            #     'value': CatFaceLandmark.LEFT_EYE_BELOW,
            #     'name': 'Left Eye Below'
            # },
            
            {
                'value': CatFaceLandmark.LEFT_OF_LEFT_EAR,
                'name': 'Left of Left Ear'
            },
            {
                'value': CatFaceLandmark.LEFT_OF_RIGHT_EAR,
                'name': 'Left of Right Ear'
            },
            {
                'value': CatFaceLandmark.NOSE,
                'name': 'Nose'
            },
            # {
            #     'value': CatFaceLandmark.NOSE_LEFT,
            #     'name': 'Nose Left'
            # },
            # {
            #     'value': CatFaceLandmark.NOSE_RIGHT,
            #     'name': 'Nose Right'
            # },
            # {
            #     'value': CatFaceLandmark.NOSE_BELOW,
            #     'name': 'Nose Below'
            # },
            {
                'value': CatFaceLandmark.RIGHT_EYE,
                'name': 'Right Eye'
            },
            # {
            #     'value': CatFaceLandmark.RIGHT_EYE_LEFT,
            #     'name': 'Right Eye Left'
            # },
            # {
            #     'value': CatFaceLandmark.RIGHT_EYE_RIGHT,
            #     'name': 'Right Eye Right'
            # },
            # {
            #     'value': CatFaceLandmark.RIGHT_EYE_ABOVE,
            #     'name': 'Right Eye Above'
            # },
            # {
            #     'value': CatFaceLandmark.RIGHT_EYE_BELOW,
            #     'name': 'Right Eye Below'
            # },
            {
                'value': CatFaceLandmark.RIGHT_OF_LEFT_EAR,
                'name': 'Right of Left Ear'
            },
            {
                'value': CatFaceLandmark.RIGHT_OF_RIGHT_EAR,
                'name': 'Right of Right Ear'
            }
        ]
