package engineTester;

import java.util.ArrayList;
import particles.*;
import guis.*;
import java.util.List;
import java.util.Random;

import models.RawModel;
import models.TexturedModel;
import objConverter.ModelData;
import objConverter.OBJFileLoader;
import particles.Particle;
import particles.ParticleMaster;

import org.lwjgl.input.Keyboard;
import org.lwjgl.opengl.Display;
import org.lwjgl.util.vector.*;

import textures.*;
import renderEngine.DisplayManager;
import renderEngine.Loader;
import renderEngine.MasterRenderer;
import renderEngine.OBJLoader;
import terrains.Terrain;
import textures.ModelTexture;
import entities.Camera;
import entities.Entity;
import entities.Light;
import entities.*;

public class MainGameLoop {

	public static void main(String[] args) {

		DisplayManager.createDisplay();
		Loader loader = new Loader();
		
		TerrainTexture modelTexture = new TerrainTexture(loader.loadTexture("space"));
		TerrainTexture rTexture = new TerrainTexture(loader.loadTexture("cloud"));
		TerrainTexture gTexture = new TerrainTexture(loader.loadTexture("starPath"));
		TerrainTexture bTexture = new TerrainTexture(loader.loadTexture("flowerpath"));
		
		TerrainTexturePack texturePack = new TerrainTexturePack(modelTexture, rTexture,
				bTexture, gTexture);
		TerrainTexture blendMap = new TerrainTexture(loader.loadTexture("blendMap"));
		
		ModelData data = OBJFileLoader.loadOBJ("ringplanets");
		
		RawModel model = loader.loadToVAO(data.getVertices(), data.getTextureCoords(), 
				data.getNormals(), data.getIndices());
		
		TexturedModel staticModel = new TexturedModel(model,new ModelTexture(loader.loadTexture("earth")));
		TexturedModel lamp = new TexturedModel(OBJLoader.loadObjModel("lamp2", loader), new ModelTexture(loader.loadTexture("metal")));
		TexturedModel earth = new TexturedModel(OBJLoader.loadObjModel("sphere", loader), new ModelTexture(loader.loadTexture("earth")));
		lamp.getTexture().setUseFakeLighting(true);
		
		
		TexturedModel sun = new TexturedModel(OBJLoader.loadObjModel("sphere", loader), new ModelTexture(loader.loadTexture("sun")));
		lamp.getTexture().setUseFakeLighting(true);
		
		TexturedModel saturn = new TexturedModel(OBJLoader.loadObjModel("ringplanets", loader), new ModelTexture(loader.loadTexture("saturn")));
		lamp.getTexture().setUseFakeLighting(true);
		
		TexturedModel mars = new TexturedModel(OBJLoader.loadObjModel("sphere", loader), new ModelTexture(loader.loadTexture("mars")));
		lamp.getTexture().setUseFakeLighting(true);
		
		TexturedModel jupiter = new TexturedModel(OBJLoader.loadObjModel("ringplanets", loader), new ModelTexture(loader.loadTexture("jupiter")));
		lamp.getTexture().setUseFakeLighting(true);
		
		TexturedModel venus = new TexturedModel(OBJLoader.loadObjModel("sphere", loader), new ModelTexture(loader.loadTexture("venus")));
		lamp.getTexture().setUseFakeLighting(true);
		
		TexturedModel mercury = new TexturedModel(OBJLoader.loadObjModel("sphere", loader), new ModelTexture(loader.loadTexture("mercury")));
		lamp.getTexture().setUseFakeLighting(true);
		
		TexturedModel neptune = new TexturedModel(OBJLoader.loadObjModel("ringplanets", loader), new ModelTexture(loader.loadTexture("neptune")));
		lamp.getTexture().setUseFakeLighting(true);
		
		TexturedModel uranus = new TexturedModel(OBJLoader.loadObjModel("ringplanets", loader), new ModelTexture(loader.loadTexture("uranus")));
		lamp.getTexture().setUseFakeLighting(true);
		
		TexturedModel grass = new TexturedModel(OBJLoader.loadObjModel("grassModel", loader), new ModelTexture(loader.loadTexture("star3")));
		grass.getTexture().setHasTransparency(true);
		grass.getTexture().setUseFakeLighting(true);
		
		ModelTexture fernTextureAtlas = new ModelTexture(loader.loadTexture("heart"));
		fernTextureAtlas.setNumberOfRows(2);
		
		TexturedModel fern = new TexturedModel(OBJLoader.loadObjModel("fern", loader),
				fernTextureAtlas);
		fern.getTexture().setHasTransparency(true);
		List<Entity> entities = new ArrayList<Entity>();
		Random random = new Random();
		List<Light> lights = new ArrayList<Light>();
		lights.add(new Light(new Vector3f(0, 1000, -7000), new Vector3f(1, 1, 1)));
		//the planets light
		lights.add(new Light(new Vector3f(185, 25, -293), new Vector3f(2, 0, 0), new Vector3f(1, 0.01f, 0.002f)));
		lights.add(new Light(new Vector3f(370, 25, -300), new Vector3f(0, 2, 2), new Vector3f(1, 0.01f, 0.002f)));
		lights.add(new Light(new Vector3f(293, 25, -305), new Vector3f(2, 2, 0), new Vector3f(1, 0.01f, 0.002f)));
		lights.add(new Light(new Vector3f(305, 25, -500), new Vector3f(2, 2, 3), new Vector3f(1, 0.01f, 0.002f)));
		lights.add(new Light(new Vector3f(195, 25, -100), new Vector3f(2, 5, 4), new Vector3f(1, 0.01f, 0.002f)));
		lights.add(new Light(new Vector3f(145, 25, -400), new Vector3f(2, 4, 2), new Vector3f(1, 0.01f, 0.002f)));
		lights.add(new Light(new Vector3f(200, 25, -450), new Vector3f(2, 3, 3), new Vector3f(1, 0.01f, 0.002f)));
		lights.add(new Light(new Vector3f(305, 25, -200), new Vector3f(3, 4, 2), new Vector3f(1, 0.01f, 0.002f)));
		lights.add(new Light(new Vector3f(400, 25, -500), new Vector3f(3, 4, 5), new Vector3f(1, 0.01f, 0.002f)));
		
		entities.add(new Entity(earth, new Vector3f(185, 25, -293), 0,0,0,3));  // index 0
		entities.add(new Entity(lamp, new Vector3f(185, 0, -293), 0,0,0,3));
		entities.add(new Entity(sun, new Vector3f(370, 100, -300), 0,0,0,50));    // index 2
		entities.add(new Entity(lamp, new Vector3f(370, 0, -300), 0,0,0,6));
		entities.add(new Entity(saturn, new Vector3f(293, 50, -305), 0,0,0,13));    // index 4
		entities.add(new Entity(lamp, new Vector3f(293, 0, -305), 0,0,0,5));
		entities.add(new Entity(mars, new Vector3f(305, 25, -500), 0,0,0,2));    // index 6
		entities.add(new Entity(lamp, new Vector3f(305, 0, -500), 0,0,0,3));
		entities.add(new Entity(venus, new Vector3f(195, 25, -100), 0,0,0,3));    // index 8
		entities.add(new Entity(lamp, new Vector3f(195, 0, -100), 0,0,0,3));
		entities.add(new Entity(mercury, new Vector3f(145, 25, -400), 0,0,0,1));    // index 10
		entities.add(new Entity(lamp, new Vector3f(145, 0, -400), 0,0,0,3));
		entities.add(new Entity(jupiter, new Vector3f(200, 55, -450), 0,0,0,15));    // index 12
		entities.add(new Entity(lamp, new Vector3f(200, 0, -450), 0,0,0,5));
		entities.add(new Entity(uranus, new Vector3f(305, 40, -200), 0,0,0,7));    // index 14
		entities.add(new Entity(lamp, new Vector3f(305, 0, -200), 0,0,0,4));
		entities.add(new Entity(neptune, new Vector3f(400, 35, -500), 0,0,0,5));    // index 14
		entities.add(new Entity(lamp, new Vector3f(400, 0, -500), 0,0,0,4));
		
		Terrain terrain = new Terrain(0,-1,loader, texturePack, blendMap);
		for(int i=0;i<100;i++){
			if (i % 2 == 0) {
				float x = random.nextFloat() * 400 + 100;
				float z = random.nextFloat() * -600;
				float y = terrain.getHeightOfTerrain(x, z);
				entities.add(new Entity(grass, new Vector3f(x,y,z),0,random.nextFloat()* 360,0,2));
			
				entities.add(new Entity(fern, random.nextInt(4), new Vector3f(x, y, z), 0, random.nextFloat()* 360,0,1f));
			}
		}
		

		
		
		
		MasterRenderer renderer = new MasterRenderer(loader);
		ParticleMaster.init(loader, renderer.getProjectionMatrix());
		RawModel bunnyModel = OBJLoader.loadObjModel("f16", loader);
		TexturedModel stanfordBunny = new TexturedModel(bunnyModel, 
				new ModelTexture(loader.loadTexture("red")));
		
		Player player = new Player(stanfordBunny, new Vector3f(100, 15, -150), 0, 180,0,1);
		Camera camera = new Camera(player);
		
		
		ParticleTexture particleTexture = new ParticleTexture(loader.loadTexture("heart"), 1);
		
		ParticleSystem system = new ParticleSystem(particleTexture, 40, 10, 0.1f, 1, 1.6f);
		
		while(!Display.isCloseRequested()){
			player.move(terrain);
			camera.move();
			
			
			
			if (Keyboard.isKeyDown(Keyboard.KEY_SPACE)) {
				system.generateParticles(player.getPosition());
				
			}
			
			
			
			ParticleMaster.update();
			
			renderer.processEntity(player);
			renderer.processTerrain(terrain);
			
		
			for(Entity entity:entities){
				renderer.processEntity(entity);
			}
			
			entities.get(0).increaseRotation(0, 5, 0);
			entities.get(2).increaseRotation(0, 0.2f, 0);
			entities.get(4).increaseRotation(0, 3, 0);
			entities.get(6).increaseRotation(0, 5, 0);
			entities.get(8).increaseRotation(0, 7, 0);
			entities.get(10).increaseRotation(0, 8, 0);
			entities.get(12).increaseRotation(0, 4, 0);
			entities.get(14).increaseRotation(0, 2, 0);
			entities.get(16).increaseRotation(0, 1, 0);
			
			if (lights.get(2).getPosition().x != 400) {
				lights.get(2).getPosition().x += 0.5f;
			} else {
				lights.get(2).getPosition().x = 370;
			}
			renderer.render(lights, camera);
			ParticleMaster.renderParticles(camera);
			
			DisplayManager.updateDisplay();
			
		}
		
		ParticleMaster.cleanUp();
		renderer.cleanUp();
		loader.cleanUp();
		DisplayManager.closeDisplay();

	}

}