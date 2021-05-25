from core.main_helper import build_params, run_browser


def main():
    args = build_params()

    type = args.type
    if 'mobile' in type:
        title = args.title
        script = args.script
        reruns = args.reruns
        parallel = args.parallel
        headless = args.headless
        mock = args.mock
        testing_url = args.testing_url
        baseline_url = args.baseline_url
        run_browser(title, script, reruns, parallel, headless, mock, testing_url, baseline_url)


if __name__ == '__main__':
    main()
