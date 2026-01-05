import grpc
import course_service_pb2
import course_service_pb2_grpc


def run():
    """Запуск gRPC клиента"""
    channel = grpc.insecure_channel('localhost:50051')
    stub = course_service_pb2_grpc.CourseServiceStub(channel)
    
    request = course_service_pb2.GetCourseRequest(course_id="api-course")
    
    try:
        response = stub.GetCourse(request)
        
        print(response)
        
    except grpc.RpcError as e:
        print(f"Ошибка при вызове gRPC сервера: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    run()