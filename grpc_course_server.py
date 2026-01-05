# grpc_course_server.py
import grpc
from concurrent import futures
import course_service_pb2
import course_service_pb2_grpc


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация сервиса курсов"""
    
    def GetCourse(self, request, context):
        """Обработчик метода GetCourse"""
        print(f"Получен запрос на курс с ID: {request.course_id}")
        
        response = course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов"
        )
        
        return response


def serve():
    """Запуск gRPC сервера"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(
        CourseServiceServicer(), server
    )
    
    port = '50051'
    server.add_insecure_port(f'[::]:{port}')
    
    server.start()
    print(f"gRPC сервер запущен на порту {port}")
    print("Ожидание запросов...")
    
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("\nСервер остановлен")
        server.stop(0)


if __name__ == '__main__':
    serve()