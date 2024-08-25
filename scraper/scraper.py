import docker
from flask import Flask, jsonify

app = Flask(__name__)

client = docker.from_env()

@app.route('/metrics')
def metrics():
    try:
        container_a = client.containers.get('docker-challenge')
        stats = container_a.stats(stream=False)
        cpu_usage = stats['cpu_stats']['cpu_usage']['total_usage']
        memory_usage = stats['memory_stats']['usage']
        memory_limit = stats['memory_stats']['limit']
        metrics_data = {'cpu_usage': cpu_usage,'memory_usage': memory_usage,'memory_limit': memory_limit}

        return jsonify(metrics_data)

    except Exception as err:
        return jsonify({'error': str(err)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
