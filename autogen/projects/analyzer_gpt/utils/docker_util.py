from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import WORK_DIR_DOCKER,TIMEOUT_DOCKER

def getDockerComandLineExceutor():
    docker = DockerCommandLineCodeExecutor(
        work_dir=WORK_DIR_DOCKER
        timeout=TIMEOUT_DOCKER
    )
    return docker

async def start_docker_container(docker):
    print("Starting Docker Conatiner......")
    await docker.start()
    print("Docker Container started")

async def stop_docker_container(docker):
    
