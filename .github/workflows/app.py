@app.route("/jobs", methods=["GET"])
def get_jobs_api():
    skill = request.args.get("skill")

    if skill:
        filtered = [job for job in jobs_data if skill.lower() in job["skills"].lower()]
        return jsonify(filtered)

    return jsonify(jobs_data)
