from aiohttp import web
import uuid

app = web.Application()


class CCTV_frame:
    def __init__(
        self,
        frame_id,
        location_x,
        location_y,
        frame_rate,
        camera_status,
        zoom_level,
        ip_address,
    ):

        self.frame_id = frame_id
        self.location_x = location_x
        self.location_y = location_y
        self.frame_rate = frame_rate
        self.camera_status = camera_status
        self.zoom_level = zoom_level
        self.ip_address = ip_address

    def info(self):
        print(
            f"frame_id: {self.frame_id }, location: ({self.location_x}, {self.location_y }), frame_rate: {self.frame_rate}, camera_status: {self.camera_status}, zoom_level: {self.zoom_level }, ip_address: {self.ip_address}"
        )

    def update_location(self, x, y):
        self.location_x = x
        self.location_y = y

    async def new_instance(request):
        data = await request.json()

        instance = CCTV_frame(
            uuid.uuid4(),
            data["cctv_details"]["location_x"],
            data["cctv_details"]["location_y"],
            data["cctv_details"]["frame_rate"],
            data["cctv_details"]["camera_status"],
            data["cctv_details"]["zoom_level"],
            data["cctv_details"]["ip_address"],
        )

        data = instance.info()
        if instance != None:
            return web.json_response(
                {
                    "message": f"Frame ID: {instance.frame_id} , Location: {(instance.location_x, instance.location_y)}, Frame rate: 30, Camera status: Active, Zoom level: 1x, IP address: 192.168.5.11"
                }
            )

    app.router.add_post("/cctv", new_instance)


if __name__ == "__main__":
    web.run_app(app, port=8080)
