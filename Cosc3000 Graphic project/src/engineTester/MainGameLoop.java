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
		TerrainTexture bTexture = new TerrainTexture(loader.loadTexture("path"));
		
		TerrainTexturePack texturePack = new TerrainTexturePack(modelTexture, rTexture,
				bTexture, gTexture);
		TerrainTexture blendMap = new TerrainTexture(loader.loadTexture("blendMap"));
		
		ModelData data = OBJFileLoader.loadOBJ("ringplanets");
		
		RawModel model = loader.loadToVAO(data.getVertices(), data.getTextureCoords(), 
				data.getNormals(), data.getIndices());
		
		TexturedModel staticModel = new TexturedModel(model,new ModelTexture(loader.loadTexture("earth")));
		TexturedModel lamp = new TexturedModel(OBJLoader.loadObjModel("lamp", loader), new ModelTexture(loader.loadTexture("lamp")));
		TexturedModel earth = new TexturedModel(OBJLoader.loadObjModel("ringplanets", loader), new ModelTexture(loader.loadTexture("earth")));
		lamp.getTexture().setUseFakeLighting(true);
		
		
		TexturedModel grass = new TexturedModel(OBJLoader.loadObjModel("grassModel", loader), new ModelTexture(loader.loadTexture("grassTexture")));
		grass.getTexture().setHasTransparency(true);
		grass.getTexture().setUseFakeLighting(true);
		
		ModelTexture fernTextureAtlas = new ModelTexture(loader.loadTexture("ferns"));
		fernTextureAtlas.setNumberOfRows(2);
		
		TexturedModel fern = new TexturedModel(OBJLoader.loadObjModel("fern", loader),
				fernTextureAtlas);
		fern.getTexture().setHasTransparency(true);
		List<Entity> entities = new ArrayList<Entity>();
		Random random = new Random();
		List<Light> lights = new ArrayList<Light>();
		lights.add(new Light(new Vector3f(0, 1000, -7000), new Vector3f(3, 3, 3)));
		lights.add(new Light(new Vector3f(185, 15, -293), new Vector3f(2, 0, 0), new Vector3f(1, 0.01f, 0.002f)));
		lights.add(new Light(new Vector3f(370, 15, -300), new Vector3f(0, 2, 2), new Vector3f(1, 0.01f, 0.002f)));
		lights.add(new Light(new Vector3f(293, 15, -305), new Vector3f(2, 2, 0), new Vector3f(1, 0.01f, 0.002f)));
		
		entities.add(new Entity(earth, new Vector3f(185, 10, -293), 0,0,0,3));
		entities.add(new Entity(lamp, new Vector3f(370, 0, -300), 0,0,0,1));
		entities.add(new Entity(lamp, new Vector3f(293, 0, -305), 0,0,0,1));
		Terrain terrain = new Terrain(0,-1,loader, texturePack, blendMap);
		for(int i=0;i<400;i++){
			if (i % 2 == 0) {
				float x = random.nextFloat() * 800 - 400;
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
				new ModelTexture(loader.loadTexture("metal")));
		
		Player player = new Player(stanfordBunny, new Vector3f(100, 15, -150), 0, 180,0,1);
		Camera camera = new Camera(player);
		
		
		
		
		
		
		while(!Display.isCloseRequested()){
			player.move(terrain);
			camera.move();
			
			if (Keyboard.isKeyDown(Keyboard.KEY_SPACE)) {
				new Particle(new Vector3f(player.getPosition()), new Vector3f(0, 30, 0), 1, 4, 0,
						1);
				
			}
			
			
			
			ParticleMaster.update();
			
			renderer.processEntity(player);
			renderer.processTerrain(terrain);
			
		
			for(Entity entity:entities){
				renderer.processEntity(entity);
			}
			
			entities.get(0).increaseRotation(0, 1, 0);
			
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