import os
import argparse
from tqdm import tqdm

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--model-path', type = str, required = True)
	parser.add_argument('--render-path', type = str, required = True)
	parser.add_argument('--blender-path', type = str, required = True)
	arguments = parser.parse_args()

	model_paths = []
	render_paths = []
	for category in os.listdir(arguments.model_path):
		for model in os.listdir(os.path.join(arguments.model_path, category)):
			model_paths.append(os.path.join(arguments.model_path, category, model, 'models', 'model_normalized.obj'))
			render_paths.append(os.path.join(arguments.render_path, category, model))
	
	for model_path, render_path in tqdm(zip(model_paths, render_paths)):
		os.makedirs(render_path, exist_ok = True)
		try:
			os.system(arguments.blender_path + ' --background --python render_blender.py -- --views %d --obj_save_dir %s %s > /dev/null 2>&1' % (72, render_path, model_path))
		except Exception:
			print('Error!')
