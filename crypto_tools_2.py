
def main() -> None:
    """
    Get images list and annotations list from input dir.
    Update new images and annotations.
    Save images and annotations in output dir.
    """
    img_paths, annos = get_dataset(LABEL_DIR, IMG_DIR)
    for index in range(NUMBER_IMAGES):
        idxs = random.sample(range(len(annos)), 4)
        new_image, new_annos, path = update_image_and_anno(
            img_paths,
            annos,
            idxs,
            OUTPUT_SIZE,
            SCALE_RANGE,
            filter_scale=FILTER_TINY_SCALE,
        )


def config_key(self, value):
        self.__config_key = self.__check_attr(value, self.__config_key_size, 'config_key')


def hash_rounds(self):
        return self.__hash_rounds


def serialize(self, data=None, filters=None):
        if filters is None:
            filters = {"rest", "relations", "resource_name"}
        if data is None:
            data = {}


def get(self, data=None, headers=None):
        if headers is None:
            headers = {}
        if data is None:
            data = {}
        return self.query(method="get", data=json.dumps(self.serialize(data)), headers=self.build_headers(headers))


def put(self, data=None, headers=None):
        if data is None:
            data = {}
        if headers is None:
            headers = {}
        return self.query(method="put", data=json.dumps(self.serialize(data)), headers=self.build_headers(headers))

