cmd = "docker build -t 155215722524.dkr.ecr.eu-central-1.amazonaws.com/calc:develop-44-ARM64 . -f Dockerfile --build-arg GITHUB_TOKEN=***"

tmp = """ARG1=1
ARG2=2
ARG3=3
"""

res = " --build-arg ".join(line.strip() for line in tmp.splitlines())
if len(res) != 0:
    res = "--build-arg " + res

print(res)
