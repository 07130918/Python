import asyncio
import asyncio.subprocess
import sys


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    print(stdout.decode())
    exitcode = await proc.wait()
    print(exitcode)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([
    run('ls -al'), run('date')
]))
